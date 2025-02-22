# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/auth/signed_message.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# third party
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n$proto/core/auth/signed_message.proto\x12\x0esyft.core.auth\x1a%proto/core/common/common_object.proto\x1a\x1bgoogle/protobuf/empty.proto"\x80\x01\n\rSignedMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x10\n\x08obj_type\x18\x02 \x01(\t\x12\x11\n\tsignature\x18\x03 \x01(\x0c\x12\x12\n\nverify_key\x18\x04 \x01(\x0c\x12\x0f\n\x07message\x18\x05 \x01(\x0c"\x1f\n\tVerifyKey\x12\x12\n\nverify_key\x18\x01 \x01(\x0c"0\n\tVerifyAll\x12#\n\x03\x61ll\x18\x01 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3'
)


_SIGNEDMESSAGE = DESCRIPTOR.message_types_by_name["SignedMessage"]
_VERIFYKEY = DESCRIPTOR.message_types_by_name["VerifyKey"]
_VERIFYALL = DESCRIPTOR.message_types_by_name["VerifyAll"]
SignedMessage = _reflection.GeneratedProtocolMessageType(
    "SignedMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _SIGNEDMESSAGE,
        "__module__": "proto.core.auth.signed_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.auth.SignedMessage)
    },
)
_sym_db.RegisterMessage(SignedMessage)

VerifyKey = _reflection.GeneratedProtocolMessageType(
    "VerifyKey",
    (_message.Message,),
    {
        "DESCRIPTOR": _VERIFYKEY,
        "__module__": "proto.core.auth.signed_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.auth.VerifyKey)
    },
)
_sym_db.RegisterMessage(VerifyKey)

VerifyAll = _reflection.GeneratedProtocolMessageType(
    "VerifyAll",
    (_message.Message,),
    {
        "DESCRIPTOR": _VERIFYALL,
        "__module__": "proto.core.auth.signed_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.auth.VerifyAll)
    },
)
_sym_db.RegisterMessage(VerifyAll)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _SIGNEDMESSAGE._serialized_start = 125
    _SIGNEDMESSAGE._serialized_end = 253
    _VERIFYKEY._serialized_start = 255
    _VERIFYKEY._serialized_end = 286
    _VERIFYALL._serialized_start = 288
    _VERIFYALL._serialized_end = 336
# @@protoc_insertion_point(module_scope)
