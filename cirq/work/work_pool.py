# Copyright 2019 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import collections
from typing import Optional, Awaitable, TypeVar, Generic

TWork = TypeVar('TWork')


class CompletionOrderedAsyncWorkPool(Generic[TWork]):
    """Ensures given work is executing, and exposes it in completion order."""

    def __init__(self, loop: Optional[asyncio.AbstractEventLoop] = None):
        self._loop = loop if loop is not None else asyncio.get_event_loop()
        self._allow_anext = asyncio.Semaphore(value=0)
        self._no_more_work_coming = False
        self._done_event = asyncio.Future()
        self._work_queue = collections.deque()
        self._out_queue = collections.deque()

    def include_work(self, work: Awaitable[TWork]) -> None:
        """Adds asynchronous work into the pool and begins executing it."""
        assert not self._no_more_work_coming
        output = asyncio.Future()
        self._out_queue.append(output)
        self._work_queue.append(output)
        asyncio.ensure_future(self._async_handle_work_completion(work),
                              loop=self._loop)

    @property
    def num_active(self) -> int:
        """The amount of work in the pool that has not completed."""
        return len(self._work_queue)

    @property
    def num_uncollected(self) -> int:
        """The amount of work still in the pool that has completed."""
        return len(self._out_queue)

    async def _async_handle_work_completion(self, work: Awaitable[TWork]):
        try:
            result = await work
            self._work_queue.popleft().set_result(result)
        except BaseException as ex:
            self._work_queue.popleft().set_exception(ex)
        self._react_to_progress()

    def _react_to_progress(self) -> None:
        """Common cleanup after something interesting happens."""
        if self._no_more_work_coming and not self._out_queue:
            self._done_event.set_result(True)
        self._allow_anext.release()

    def set_all_work_received_flag(self) -> None:
        """Indicates to the work pool that no more work will be added."""
        assert not self._no_more_work_coming
        self._react_to_progress()

    async def _anext_helper(self) -> TWork:
        await self._allow_anext.acquire()
        if self._out_queue:
            return await self._out_queue.popleft()
        else:
            self._allow_anext.release()
            raise StopAsyncIteration('no_more_work')

    def __anext__(self) -> TWork:
        return asyncio.ensure_future(self._anext_helper())

    async def async_all_done(self) -> None:
        """An awaitable that completes once all work is completed.

        Note: all work is completed only after the `set_all_work_received_flag`
        method is called, and then all work still in the pool completes.
        """
        await self._done_event

    def __aiter__(self):
        return self