# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config_routing/grpc/config_routing.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(config_routing/grpc/config_routing.proto\x12\x0e\x63onfig_routing\x1a\x1bgoogle/protobuf/empty.proto\"B\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x04name\x18\xd8\x04 \x01(\t\x12\x0e\n\x05\x65mail\x18\xf4\x03 \x01(\t\x12\x0f\n\x06groups\x18\xbc\x05 \x01(\t\"\x11\n\x0fUserListRequest\"9\n\x10UserListResponse\x12%\n\x07results\x18\x01 \x03(\x0b\x32\x14.config_routing.User\"!\n\x13UserRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\xd1\x02\n\x0eUserController\x12K\n\x04List\x12\x1f.config_routing.UserListRequest\x1a .config_routing.UserListResponse\"\x00\x12\x36\n\x06\x43reate\x12\x14.config_routing.User\x1a\x14.config_routing.User\"\x00\x12G\n\x08Retrieve\x12#.config_routing.UserRetrieveRequest\x1a\x14.config_routing.User\"\x00\x12\x36\n\x06Update\x12\x14.config_routing.User\x1a\x14.config_routing.User\"\x00\x12\x39\n\x07\x44\x65stroy\x12\x14.config_routing.User\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'config_routing.grpc.config_routing_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USER._serialized_start=89
  _USER._serialized_end=155
  _USERLISTREQUEST._serialized_start=157
  _USERLISTREQUEST._serialized_end=174
  _USERLISTRESPONSE._serialized_start=176
  _USERLISTRESPONSE._serialized_end=233
  _USERRETRIEVEREQUEST._serialized_start=235
  _USERRETRIEVEREQUEST._serialized_end=268
  _USERCONTROLLER._serialized_start=271
  _USERCONTROLLER._serialized_end=608
# @@protoc_insertion_point(module_scope)
