# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cirq/api/google/v2/program.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cirq/api/google/v2/program.proto',
  package='cirq.api.google.v2',
  syntax='proto3',
  serialized_pb=_b('\n cirq/api/google/v2/program.proto\x12\x12\x63irq.api.google.v2\"\xa6\x01\n\x07Program\x12.\n\x08language\x18\x01 \x01(\x0b\x32\x1c.cirq.api.google.v2.Language\x12.\n\x07\x63ircuit\x18\x02 \x01(\x0b\x32\x1b.cirq.api.google.v2.CircuitH\x00\x12\x30\n\x08schedule\x18\x03 \x01(\x0b\x32\x1c.cirq.api.google.v2.ScheduleH\x00\x42\t\n\x07program\"\xd4\x01\n\x07\x43ircuit\x12K\n\x13scheduling_strategy\x18\x01 \x01(\x0e\x32..cirq.api.google.v2.Circuit.SchedulingStrategy\x12+\n\x07moments\x18\x02 \x03(\x0b\x32\x1a.cirq.api.google.v2.Moment\"O\n\x12SchedulingStrategy\x12#\n\x1fSCHEDULING_STRATEGY_UNSPECIFIED\x10\x00\x12\x14\n\x10MOMENT_BY_MOMENT\x10\x01\";\n\x06Moment\x12\x31\n\noperations\x18\x01 \x03(\x0b\x32\x1d.cirq.api.google.v2.Operation\"P\n\x08Schedule\x12\x44\n\x14scheduled_operations\x18\x03 \x03(\x0b\x32&.cirq.api.google.v2.ScheduledOperation\"`\n\x12ScheduledOperation\x12\x30\n\toperation\x18\x01 \x01(\x0b\x32\x1d.cirq.api.google.v2.Operation\x12\x18\n\x10start_time_picos\x18\x02 \x01(\x03\";\n\x08Language\x12\x10\n\x08gate_set\x18\x01 \x01(\t\x12\x1d\n\x15\x61rg_function_language\x18\x02 \x01(\t\"\xdb\x01\n\tOperation\x12&\n\x04gate\x18\x01 \x01(\x0b\x32\x18.cirq.api.google.v2.Gate\x12\x35\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\'.cirq.api.google.v2.Operation.ArgsEntry\x12)\n\x06qubits\x18\x03 \x03(\x0b\x32\x19.cirq.api.google.v2.Qubit\x1a\x44\n\tArgsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.cirq.api.google.v2.Arg:\x02\x38\x01\"\x12\n\x04Gate\x12\n\n\x02id\x18\x01 \x01(\t\"\x13\n\x05Qubit\x12\n\n\x02id\x18\x02 \x01(\t\"\x82\x01\n\x03\x41rg\x12\x31\n\targ_value\x18\x01 \x01(\x0b\x32\x1c.cirq.api.google.v2.ArgValueH\x00\x12\x10\n\x06symbol\x18\x02 \x01(\tH\x00\x12/\n\x04\x66unc\x18\x03 \x01(\x0b\x32\x1f.cirq.api.google.v2.ArgFunctionH\x00\x42\x05\n\x03\x61rg\"\x82\x01\n\x08\x41rgValue\x12\x15\n\x0b\x66loat_value\x18\x01 \x01(\x02H\x00\x12:\n\x0b\x62ool_values\x18\x02 \x01(\x0b\x32#.cirq.api.google.v2.RepeatedBooleanH\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x42\x0b\n\targ_value\"!\n\x0fRepeatedBoolean\x12\x0e\n\x06values\x18\x01 \x03(\x08\"B\n\x0b\x41rgFunction\x12\x0c\n\x04type\x18\x01 \x01(\t\x12%\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x17.cirq.api.google.v2.ArgB/\n\x1d\x63om.google.cirq.api.google.v2B\x0cProgramProtoP\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CIRCUIT_SCHEDULINGSTRATEGY = _descriptor.EnumDescriptor(
  name='SchedulingStrategy',
  full_name='cirq.api.google.v2.Circuit.SchedulingStrategy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCHEDULING_STRATEGY_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOMENT_BY_MOMENT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=359,
  serialized_end=438,
)
_sym_db.RegisterEnumDescriptor(_CIRCUIT_SCHEDULINGSTRATEGY)


_PROGRAM = _descriptor.Descriptor(
  name='Program',
  full_name='cirq.api.google.v2.Program',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='cirq.api.google.v2.Program.language', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='circuit', full_name='cirq.api.google.v2.Program.circuit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='schedule', full_name='cirq.api.google.v2.Program.schedule', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='program', full_name='cirq.api.google.v2.Program.program',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=57,
  serialized_end=223,
)


_CIRCUIT = _descriptor.Descriptor(
  name='Circuit',
  full_name='cirq.api.google.v2.Circuit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scheduling_strategy', full_name='cirq.api.google.v2.Circuit.scheduling_strategy', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moments', full_name='cirq.api.google.v2.Circuit.moments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CIRCUIT_SCHEDULINGSTRATEGY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=438,
)


_MOMENT = _descriptor.Descriptor(
  name='Moment',
  full_name='cirq.api.google.v2.Moment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='cirq.api.google.v2.Moment.operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=440,
  serialized_end=499,
)


_SCHEDULE = _descriptor.Descriptor(
  name='Schedule',
  full_name='cirq.api.google.v2.Schedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scheduled_operations', full_name='cirq.api.google.v2.Schedule.scheduled_operations', index=0,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=581,
)


_SCHEDULEDOPERATION = _descriptor.Descriptor(
  name='ScheduledOperation',
  full_name='cirq.api.google.v2.ScheduledOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='cirq.api.google.v2.ScheduledOperation.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time_picos', full_name='cirq.api.google.v2.ScheduledOperation.start_time_picos', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=583,
  serialized_end=679,
)


_LANGUAGE = _descriptor.Descriptor(
  name='Language',
  full_name='cirq.api.google.v2.Language',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gate_set', full_name='cirq.api.google.v2.Language.gate_set', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arg_function_language', full_name='cirq.api.google.v2.Language.arg_function_language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=681,
  serialized_end=740,
)


_OPERATION_ARGSENTRY = _descriptor.Descriptor(
  name='ArgsEntry',
  full_name='cirq.api.google.v2.Operation.ArgsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cirq.api.google.v2.Operation.ArgsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='cirq.api.google.v2.Operation.ArgsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=894,
  serialized_end=962,
)

_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='cirq.api.google.v2.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gate', full_name='cirq.api.google.v2.Operation.gate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='cirq.api.google.v2.Operation.args', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qubits', full_name='cirq.api.google.v2.Operation.qubits', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_OPERATION_ARGSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=743,
  serialized_end=962,
)


_GATE = _descriptor.Descriptor(
  name='Gate',
  full_name='cirq.api.google.v2.Gate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cirq.api.google.v2.Gate.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=964,
  serialized_end=982,
)


_QUBIT = _descriptor.Descriptor(
  name='Qubit',
  full_name='cirq.api.google.v2.Qubit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cirq.api.google.v2.Qubit.id', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=984,
  serialized_end=1003,
)


_ARG = _descriptor.Descriptor(
  name='Arg',
  full_name='cirq.api.google.v2.Arg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arg_value', full_name='cirq.api.google.v2.Arg.arg_value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='cirq.api.google.v2.Arg.symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='func', full_name='cirq.api.google.v2.Arg.func', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='arg', full_name='cirq.api.google.v2.Arg.arg',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1006,
  serialized_end=1136,
)


_ARGVALUE = _descriptor.Descriptor(
  name='ArgValue',
  full_name='cirq.api.google.v2.ArgValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='float_value', full_name='cirq.api.google.v2.ArgValue.float_value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bool_values', full_name='cirq.api.google.v2.ArgValue.bool_values', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='cirq.api.google.v2.ArgValue.string_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='arg_value', full_name='cirq.api.google.v2.ArgValue.arg_value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1139,
  serialized_end=1269,
)


_REPEATEDBOOLEAN = _descriptor.Descriptor(
  name='RepeatedBoolean',
  full_name='cirq.api.google.v2.RepeatedBoolean',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='cirq.api.google.v2.RepeatedBoolean.values', index=0,
      number=1, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1271,
  serialized_end=1304,
)


_ARGFUNCTION = _descriptor.Descriptor(
  name='ArgFunction',
  full_name='cirq.api.google.v2.ArgFunction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='cirq.api.google.v2.ArgFunction.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='cirq.api.google.v2.ArgFunction.args', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1306,
  serialized_end=1372,
)

_PROGRAM.fields_by_name['language'].message_type = _LANGUAGE
_PROGRAM.fields_by_name['circuit'].message_type = _CIRCUIT
_PROGRAM.fields_by_name['schedule'].message_type = _SCHEDULE
_PROGRAM.oneofs_by_name['program'].fields.append(
  _PROGRAM.fields_by_name['circuit'])
_PROGRAM.fields_by_name['circuit'].containing_oneof = _PROGRAM.oneofs_by_name['program']
_PROGRAM.oneofs_by_name['program'].fields.append(
  _PROGRAM.fields_by_name['schedule'])
_PROGRAM.fields_by_name['schedule'].containing_oneof = _PROGRAM.oneofs_by_name['program']
_CIRCUIT.fields_by_name['scheduling_strategy'].enum_type = _CIRCUIT_SCHEDULINGSTRATEGY
_CIRCUIT.fields_by_name['moments'].message_type = _MOMENT
_CIRCUIT_SCHEDULINGSTRATEGY.containing_type = _CIRCUIT
_MOMENT.fields_by_name['operations'].message_type = _OPERATION
_SCHEDULE.fields_by_name['scheduled_operations'].message_type = _SCHEDULEDOPERATION
_SCHEDULEDOPERATION.fields_by_name['operation'].message_type = _OPERATION
_OPERATION_ARGSENTRY.fields_by_name['value'].message_type = _ARG
_OPERATION_ARGSENTRY.containing_type = _OPERATION
_OPERATION.fields_by_name['gate'].message_type = _GATE
_OPERATION.fields_by_name['args'].message_type = _OPERATION_ARGSENTRY
_OPERATION.fields_by_name['qubits'].message_type = _QUBIT
_ARG.fields_by_name['arg_value'].message_type = _ARGVALUE
_ARG.fields_by_name['func'].message_type = _ARGFUNCTION
_ARG.oneofs_by_name['arg'].fields.append(
  _ARG.fields_by_name['arg_value'])
_ARG.fields_by_name['arg_value'].containing_oneof = _ARG.oneofs_by_name['arg']
_ARG.oneofs_by_name['arg'].fields.append(
  _ARG.fields_by_name['symbol'])
_ARG.fields_by_name['symbol'].containing_oneof = _ARG.oneofs_by_name['arg']
_ARG.oneofs_by_name['arg'].fields.append(
  _ARG.fields_by_name['func'])
_ARG.fields_by_name['func'].containing_oneof = _ARG.oneofs_by_name['arg']
_ARGVALUE.fields_by_name['bool_values'].message_type = _REPEATEDBOOLEAN
_ARGVALUE.oneofs_by_name['arg_value'].fields.append(
  _ARGVALUE.fields_by_name['float_value'])
_ARGVALUE.fields_by_name['float_value'].containing_oneof = _ARGVALUE.oneofs_by_name['arg_value']
_ARGVALUE.oneofs_by_name['arg_value'].fields.append(
  _ARGVALUE.fields_by_name['bool_values'])
_ARGVALUE.fields_by_name['bool_values'].containing_oneof = _ARGVALUE.oneofs_by_name['arg_value']
_ARGVALUE.oneofs_by_name['arg_value'].fields.append(
  _ARGVALUE.fields_by_name['string_value'])
_ARGVALUE.fields_by_name['string_value'].containing_oneof = _ARGVALUE.oneofs_by_name['arg_value']
_ARGFUNCTION.fields_by_name['args'].message_type = _ARG
DESCRIPTOR.message_types_by_name['Program'] = _PROGRAM
DESCRIPTOR.message_types_by_name['Circuit'] = _CIRCUIT
DESCRIPTOR.message_types_by_name['Moment'] = _MOMENT
DESCRIPTOR.message_types_by_name['Schedule'] = _SCHEDULE
DESCRIPTOR.message_types_by_name['ScheduledOperation'] = _SCHEDULEDOPERATION
DESCRIPTOR.message_types_by_name['Language'] = _LANGUAGE
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
DESCRIPTOR.message_types_by_name['Gate'] = _GATE
DESCRIPTOR.message_types_by_name['Qubit'] = _QUBIT
DESCRIPTOR.message_types_by_name['Arg'] = _ARG
DESCRIPTOR.message_types_by_name['ArgValue'] = _ARGVALUE
DESCRIPTOR.message_types_by_name['RepeatedBoolean'] = _REPEATEDBOOLEAN
DESCRIPTOR.message_types_by_name['ArgFunction'] = _ARGFUNCTION

Program = _reflection.GeneratedProtocolMessageType('Program', (_message.Message,), dict(
  DESCRIPTOR = _PROGRAM,
  __module__ = 'cirq.api.google.v2.program_pb2'
  # @@protoc_insertion_point(class_scope:cirq.api.google.v2.Program)
  ))
_sym_db.RegisterMessage(Program)

Circuit = _reflection.GeneratedProtocolMessageType('Circuit', (_message.Message,), dict(
  DESCRIPTOR = _CIRCUIT,
  __module__ = 'cirq.api.google.v2.program_pb2'
  # @@protoc_insertion_point(class_scope:cirq.api.google.v2.Circuit)
  ))
_sym_db.RegisterMessage(Circuit)

Moment = _reflection.GeneratedProtocolMessageType('Moment', (_message.Message,), dict(
  DESCRIPTOR = _MOMENT,
  __module__ = 'cirq.api.google.v2.program_pb2'
  # @@protoc_insertion_point(class_scope:cirq.api.google.v2.Moment)
  ))
_sym_db.RegisterMessage(Moment)

Schedule = _reflection.GeneratedProtocolMessageType('Schedule', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULE,
  __module__ = 'cirq.api.google.v2.program_pb2'
  # @@protoc_insertion_point(class_scope:cirq.api.google.v2.Schedule)
  ))
_sym_db.RegisterMessage(Schedule)

ScheduledOperation = _reflection.GeneratedProtocolMessageType('ScheduledOperation', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULEDOPERATION,
  __module__ = 'cirq.api.google.v2.program_pb2'
  # @@protoc_insertion_point(class_scope:cirq.api.google.v2.ScheduledOperation)
  ))
_sym_db.RegisterMessage(ScheduledOperation)

Language = _reflection.GeneratedProtocolMessageType('Language', (_message.Message,), dict(
  DESCRIPTOR = _LANGUAGE,
  __module__ = 'cirq.api.google.v2.program_pb2'
  # @@protoc_insertion_point(class_scope:cirq.api.google.v2.Language)
  ))
_sym_db.RegisterMessage(Language)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(

  ArgsEntry = _reflection.GeneratedProtocolMessageType('ArgsEntry', (_message.Message,), dict(
    DESCRIPTOR = _OPERATION_ARGSENTRY,
    __module__ = 'cirq.api.google.v2.program_pb2'
    # @@protoc_insertion_point(class_scope:cirq.api.google.v2.Operation.ArgsEntry)
    ))
  ,
  DESCRIPTOR = _OPERATION,
  __module__ = 'cirq.api.google.v2.program_pb2'
  # @@protoc_insertion_point(class_scope:cirq.api.google.v2.Operation)
  ))
_sym_db.RegisterMessage(Operation)
_sym_db.RegisterMessage(Operation.ArgsEntry)

Gate = _reflection.GeneratedProtocolMessageType('Gate', (_message.Message,), dict(
  DESCRIPTOR = _GATE,
  __module__ = 'cirq.api.google.v2.program_pb2'
  # @@protoc_insertion_point(class_scope:cirq.api.google.v2.Gate)
  ))
_sym_db.RegisterMessage(Gate)

Qubit = _reflection.GeneratedProtocolMessageType('Qubit', (_message.Message,), dict(
  DESCRIPTOR = _QUBIT,
  __module__ = 'cirq.api.google.v2.program_pb2'
  # @@protoc_insertion_point(class_scope:cirq.api.google.v2.Qubit)
  ))
_sym_db.RegisterMessage(Qubit)

Arg = _reflection.GeneratedProtocolMessageType('Arg', (_message.Message,), dict(
  DESCRIPTOR = _ARG,
  __module__ = 'cirq.api.google.v2.program_pb2'
  # @@protoc_insertion_point(class_scope:cirq.api.google.v2.Arg)
  ))
_sym_db.RegisterMessage(Arg)

ArgValue = _reflection.GeneratedProtocolMessageType('ArgValue', (_message.Message,), dict(
  DESCRIPTOR = _ARGVALUE,
  __module__ = 'cirq.api.google.v2.program_pb2'
  # @@protoc_insertion_point(class_scope:cirq.api.google.v2.ArgValue)
  ))
_sym_db.RegisterMessage(ArgValue)

RepeatedBoolean = _reflection.GeneratedProtocolMessageType('RepeatedBoolean', (_message.Message,), dict(
  DESCRIPTOR = _REPEATEDBOOLEAN,
  __module__ = 'cirq.api.google.v2.program_pb2'
  # @@protoc_insertion_point(class_scope:cirq.api.google.v2.RepeatedBoolean)
  ))
_sym_db.RegisterMessage(RepeatedBoolean)

ArgFunction = _reflection.GeneratedProtocolMessageType('ArgFunction', (_message.Message,), dict(
  DESCRIPTOR = _ARGFUNCTION,
  __module__ = 'cirq.api.google.v2.program_pb2'
  # @@protoc_insertion_point(class_scope:cirq.api.google.v2.ArgFunction)
  ))
_sym_db.RegisterMessage(ArgFunction)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\035com.google.cirq.api.google.v2B\014ProgramProtoP\001'))
_OPERATION_ARGSENTRY.has_options = True
_OPERATION_ARGSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
