# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/transport/internet/kcp/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray.com.core.common.serial import typed_message_pb2 as v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/transport/internet/kcp/config.proto',
  package='v2ray.core.transport.internet.kcp',
  syntax='proto3',
  serialized_pb=_b('\n2v2ray.com/core/transport/internet/kcp/config.proto\x12!v2ray.core.transport.internet.kcp\x1a\x30v2ray.com/core/common/serial/typed_message.proto\"\x14\n\x03MTU\x12\r\n\x05value\x18\x01 \x01(\r\"\x14\n\x03TTI\x12\r\n\x05value\x18\x01 \x01(\r\"\x1f\n\x0eUplinkCapacity\x12\r\n\x05value\x18\x01 \x01(\r\"!\n\x10\x44ownlinkCapacity\x12\r\n\x05value\x18\x01 \x01(\r\"\x1b\n\x0bWriteBuffer\x12\x0c\n\x04size\x18\x01 \x01(\r\"\x1a\n\nReadBuffer\x12\x0c\n\x04size\x18\x01 \x01(\r\"!\n\x0f\x43onnectionReuse\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\"\xf1\x03\n\x06\x43onfig\x12\x33\n\x03mtu\x18\x01 \x01(\x0b\x32&.v2ray.core.transport.internet.kcp.MTU\x12\x33\n\x03tti\x18\x02 \x01(\x0b\x32&.v2ray.core.transport.internet.kcp.TTI\x12J\n\x0fuplink_capacity\x18\x03 \x01(\x0b\x32\x31.v2ray.core.transport.internet.kcp.UplinkCapacity\x12N\n\x11\x64ownlink_capacity\x18\x04 \x01(\x0b\x32\x33.v2ray.core.transport.internet.kcp.DownlinkCapacity\x12\x12\n\ncongestion\x18\x05 \x01(\x08\x12\x44\n\x0cwrite_buffer\x18\x06 \x01(\x0b\x32..v2ray.core.transport.internet.kcp.WriteBuffer\x12\x42\n\x0bread_buffer\x18\x07 \x01(\x0b\x32-.v2ray.core.transport.internet.kcp.ReadBuffer\x12=\n\rheader_config\x18\x08 \x01(\x0b\x32&.v2ray.core.common.serial.TypedMessageJ\x04\x08\t\x10\nBR\n%com.v2ray.core.transport.internet.kcpP\x01Z\x03kcp\xaa\x02!V2Ray.Core.Transport.Internet.Kcpb\x06proto3')
  ,
  dependencies=[v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2.DESCRIPTOR,])




_MTU = _descriptor.Descriptor(
  name='MTU',
  full_name='v2ray.core.transport.internet.kcp.MTU',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v2ray.core.transport.internet.kcp.MTU.value', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=139,
  serialized_end=159,
)


_TTI = _descriptor.Descriptor(
  name='TTI',
  full_name='v2ray.core.transport.internet.kcp.TTI',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v2ray.core.transport.internet.kcp.TTI.value', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=161,
  serialized_end=181,
)


_UPLINKCAPACITY = _descriptor.Descriptor(
  name='UplinkCapacity',
  full_name='v2ray.core.transport.internet.kcp.UplinkCapacity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v2ray.core.transport.internet.kcp.UplinkCapacity.value', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=183,
  serialized_end=214,
)


_DOWNLINKCAPACITY = _descriptor.Descriptor(
  name='DownlinkCapacity',
  full_name='v2ray.core.transport.internet.kcp.DownlinkCapacity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v2ray.core.transport.internet.kcp.DownlinkCapacity.value', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=216,
  serialized_end=249,
)


_WRITEBUFFER = _descriptor.Descriptor(
  name='WriteBuffer',
  full_name='v2ray.core.transport.internet.kcp.WriteBuffer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='v2ray.core.transport.internet.kcp.WriteBuffer.size', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=251,
  serialized_end=278,
)


_READBUFFER = _descriptor.Descriptor(
  name='ReadBuffer',
  full_name='v2ray.core.transport.internet.kcp.ReadBuffer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='v2ray.core.transport.internet.kcp.ReadBuffer.size', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=280,
  serialized_end=306,
)


_CONNECTIONREUSE = _descriptor.Descriptor(
  name='ConnectionReuse',
  full_name='v2ray.core.transport.internet.kcp.ConnectionReuse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable', full_name='v2ray.core.transport.internet.kcp.ConnectionReuse.enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=308,
  serialized_end=341,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.transport.internet.kcp.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mtu', full_name='v2ray.core.transport.internet.kcp.Config.mtu', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tti', full_name='v2ray.core.transport.internet.kcp.Config.tti', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uplink_capacity', full_name='v2ray.core.transport.internet.kcp.Config.uplink_capacity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='downlink_capacity', full_name='v2ray.core.transport.internet.kcp.Config.downlink_capacity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='congestion', full_name='v2ray.core.transport.internet.kcp.Config.congestion', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='write_buffer', full_name='v2ray.core.transport.internet.kcp.Config.write_buffer', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_buffer', full_name='v2ray.core.transport.internet.kcp.Config.read_buffer', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header_config', full_name='v2ray.core.transport.internet.kcp.Config.header_config', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=344,
  serialized_end=841,
)

_CONFIG.fields_by_name['mtu'].message_type = _MTU
_CONFIG.fields_by_name['tti'].message_type = _TTI
_CONFIG.fields_by_name['uplink_capacity'].message_type = _UPLINKCAPACITY
_CONFIG.fields_by_name['downlink_capacity'].message_type = _DOWNLINKCAPACITY
_CONFIG.fields_by_name['write_buffer'].message_type = _WRITEBUFFER
_CONFIG.fields_by_name['read_buffer'].message_type = _READBUFFER
_CONFIG.fields_by_name['header_config'].message_type = v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2._TYPEDMESSAGE
DESCRIPTOR.message_types_by_name['MTU'] = _MTU
DESCRIPTOR.message_types_by_name['TTI'] = _TTI
DESCRIPTOR.message_types_by_name['UplinkCapacity'] = _UPLINKCAPACITY
DESCRIPTOR.message_types_by_name['DownlinkCapacity'] = _DOWNLINKCAPACITY
DESCRIPTOR.message_types_by_name['WriteBuffer'] = _WRITEBUFFER
DESCRIPTOR.message_types_by_name['ReadBuffer'] = _READBUFFER
DESCRIPTOR.message_types_by_name['ConnectionReuse'] = _CONNECTIONREUSE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MTU = _reflection.GeneratedProtocolMessageType('MTU', (_message.Message,), dict(
  DESCRIPTOR = _MTU,
  __module__ = 'v2ray.com.core.transport.internet.kcp.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.kcp.MTU)
  ))
_sym_db.RegisterMessage(MTU)

TTI = _reflection.GeneratedProtocolMessageType('TTI', (_message.Message,), dict(
  DESCRIPTOR = _TTI,
  __module__ = 'v2ray.com.core.transport.internet.kcp.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.kcp.TTI)
  ))
_sym_db.RegisterMessage(TTI)

UplinkCapacity = _reflection.GeneratedProtocolMessageType('UplinkCapacity', (_message.Message,), dict(
  DESCRIPTOR = _UPLINKCAPACITY,
  __module__ = 'v2ray.com.core.transport.internet.kcp.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.kcp.UplinkCapacity)
  ))
_sym_db.RegisterMessage(UplinkCapacity)

DownlinkCapacity = _reflection.GeneratedProtocolMessageType('DownlinkCapacity', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLINKCAPACITY,
  __module__ = 'v2ray.com.core.transport.internet.kcp.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.kcp.DownlinkCapacity)
  ))
_sym_db.RegisterMessage(DownlinkCapacity)

WriteBuffer = _reflection.GeneratedProtocolMessageType('WriteBuffer', (_message.Message,), dict(
  DESCRIPTOR = _WRITEBUFFER,
  __module__ = 'v2ray.com.core.transport.internet.kcp.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.kcp.WriteBuffer)
  ))
_sym_db.RegisterMessage(WriteBuffer)

ReadBuffer = _reflection.GeneratedProtocolMessageType('ReadBuffer', (_message.Message,), dict(
  DESCRIPTOR = _READBUFFER,
  __module__ = 'v2ray.com.core.transport.internet.kcp.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.kcp.ReadBuffer)
  ))
_sym_db.RegisterMessage(ReadBuffer)

ConnectionReuse = _reflection.GeneratedProtocolMessageType('ConnectionReuse', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTIONREUSE,
  __module__ = 'v2ray.com.core.transport.internet.kcp.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.kcp.ConnectionReuse)
  ))
_sym_db.RegisterMessage(ConnectionReuse)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'v2ray.com.core.transport.internet.kcp.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.kcp.Config)
  ))
_sym_db.RegisterMessage(Config)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%com.v2ray.core.transport.internet.kcpP\001Z\003kcp\252\002!V2Ray.Core.Transport.Internet.Kcp'))
# @@protoc_insertion_point(module_scope)