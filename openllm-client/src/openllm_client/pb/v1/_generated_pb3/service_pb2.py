# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\x0f\x62\x65ntoml.grpc.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x18\n\x16ServiceMetadataRequest\"\xde\x03\n\x17ServiceMetadataResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x43\n\x04\x61pis\x18\x02 \x03(\x0b\x32\x35.bentoml.grpc.v1.ServiceMetadataResponse.InferenceAPI\x12\x0c\n\x04\x64ocs\x18\x03 \x01(\t\x1ao\n\x12\x44\x65scriptorMetadata\x12\x1a\n\rdescriptor_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12+\n\nattributes\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructB\x10\n\x0e_descriptor_id\x1a\xf0\x01\n\x0cInferenceAPI\x12\x0c\n\x04name\x18\x01 \x01(\t\x12O\n\x05input\x18\x02 \x01(\x0b\x32;.bentoml.grpc.v1.ServiceMetadataResponse.DescriptorMetadataH\x00\x88\x01\x01\x12P\n\x06output\x18\x03 \x01(\x0b\x32;.bentoml.grpc.v1.ServiceMetadataResponse.DescriptorMetadataH\x01\x88\x01\x01\x12\x11\n\x04\x64ocs\x18\x04 \x01(\tH\x02\x88\x01\x01\x42\x08\n\x06_inputB\t\n\x07_outputB\x07\n\x05_docs\"\x85\x03\n\x07Request\x12\x10\n\x08\x61pi_name\x18\x01 \x01(\t\x12+\n\x07ndarray\x18\x03 \x01(\x0b\x32\x18.bentoml.grpc.v1.NDArrayH\x00\x12/\n\tdataframe\x18\x05 \x01(\x0b\x32\x1a.bentoml.grpc.v1.DataFrameH\x00\x12)\n\x06series\x18\x06 \x01(\x0b\x32\x17.bentoml.grpc.v1.SeriesH\x00\x12%\n\x04\x66ile\x18\x07 \x01(\x0b\x32\x15.bentoml.grpc.v1.FileH\x00\x12,\n\x04text\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x12&\n\x04json\x18\t \x01(\x0b\x32\x16.google.protobuf.ValueH\x00\x12/\n\tmultipart\x18\n \x01(\x0b\x32\x1a.bentoml.grpc.v1.MultipartH\x00\x12\x1a\n\x10serialized_bytes\x18\x02 \x01(\x0cH\x00\x42\t\n\x07\x63ontentJ\x04\x08\x04\x10\x05J\x04\x08\x0b\x10\x0e\"\xf4\x02\n\x08Response\x12+\n\x07ndarray\x18\x01 \x01(\x0b\x32\x18.bentoml.grpc.v1.NDArrayH\x00\x12/\n\tdataframe\x18\x03 \x01(\x0b\x32\x1a.bentoml.grpc.v1.DataFrameH\x00\x12)\n\x06series\x18\x05 \x01(\x0b\x32\x17.bentoml.grpc.v1.SeriesH\x00\x12%\n\x04\x66ile\x18\x06 \x01(\x0b\x32\x15.bentoml.grpc.v1.FileH\x00\x12,\n\x04text\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x12&\n\x04json\x18\x08 \x01(\x0b\x32\x16.google.protobuf.ValueH\x00\x12/\n\tmultipart\x18\t \x01(\x0b\x32\x1a.bentoml.grpc.v1.MultipartH\x00\x12\x1a\n\x10serialized_bytes\x18\x02 \x01(\x0cH\x00\x42\t\n\x07\x63ontentJ\x04\x08\x04\x10\x05J\x04\x08\n\x10\x0e\"\xc6\x02\n\x04Part\x12+\n\x07ndarray\x18\x01 \x01(\x0b\x32\x18.bentoml.grpc.v1.NDArrayH\x00\x12/\n\tdataframe\x18\x03 \x01(\x0b\x32\x1a.bentoml.grpc.v1.DataFrameH\x00\x12)\n\x06series\x18\x05 \x01(\x0b\x32\x17.bentoml.grpc.v1.SeriesH\x00\x12%\n\x04\x66ile\x18\x06 \x01(\x0b\x32\x15.bentoml.grpc.v1.FileH\x00\x12,\n\x04text\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x12&\n\x04json\x18\x08 \x01(\x0b\x32\x16.google.protobuf.ValueH\x00\x12\x1a\n\x10serialized_bytes\x18\x04 \x01(\x0cH\x00\x42\x10\n\x0erepresentationJ\x04\x08\x02\x10\x03J\x04\x08\t\x10\x0e\"\x89\x01\n\tMultipart\x12\x36\n\x06\x66ields\x18\x01 \x03(\x0b\x32&.bentoml.grpc.v1.Multipart.FieldsEntry\x1a\x44\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.bentoml.grpc.v1.Part:\x02\x38\x01\"3\n\x04\x46ile\x12\x11\n\x04kind\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x42\x07\n\x05_kind\"K\n\tDataFrame\x12\x14\n\x0c\x63olumn_names\x18\x01 \x03(\t\x12(\n\x07\x63olumns\x18\x02 \x03(\x0b\x32\x17.bentoml.grpc.v1.Series\"\xa1\x01\n\x06Series\x12\x17\n\x0b\x62ool_values\x18\x01 \x03(\x08\x42\x02\x10\x01\x12\x18\n\x0c\x66loat_values\x18\x02 \x03(\x02\x42\x02\x10\x01\x12\x18\n\x0cint32_values\x18\x03 \x03(\x05\x42\x02\x10\x01\x12\x18\n\x0cint64_values\x18\x06 \x03(\x03\x42\x02\x10\x01\x12\x15\n\rstring_values\x18\x05 \x03(\t\x12\x19\n\rdouble_values\x18\x04 \x03(\x01\x42\x02\x10\x01\"\xc2\x03\n\x07NDArray\x12-\n\x05\x64type\x18\x01 \x01(\x0e\x32\x1e.bentoml.grpc.v1.NDArray.DType\x12\r\n\x05shape\x18\x02 \x03(\x05\x12\x15\n\rstring_values\x18\x05 \x03(\t\x12\x18\n\x0c\x66loat_values\x18\x03 \x03(\x02\x42\x02\x10\x01\x12\x19\n\rdouble_values\x18\x04 \x03(\x01\x42\x02\x10\x01\x12\x17\n\x0b\x62ool_values\x18\x06 \x03(\x08\x42\x02\x10\x01\x12\x18\n\x0cint32_values\x18\x07 \x03(\x05\x42\x02\x10\x01\x12\x18\n\x0cint64_values\x18\x08 \x03(\x03\x42\x02\x10\x01\x12\x19\n\ruint32_values\x18\t \x03(\rB\x02\x10\x01\x12\x19\n\ruint64_values\x18\n \x03(\x04\x42\x02\x10\x01\"\xa9\x01\n\x05\x44Type\x12\x15\n\x11\x44TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x44TYPE_FLOAT\x10\x01\x12\x10\n\x0c\x44TYPE_DOUBLE\x10\x02\x12\x0e\n\nDTYPE_BOOL\x10\x03\x12\x0f\n\x0b\x44TYPE_INT32\x10\x04\x12\x0f\n\x0b\x44TYPE_INT64\x10\x05\x12\x10\n\x0c\x44TYPE_UINT32\x10\x06\x12\x10\n\x0c\x44TYPE_UINT64\x10\x07\x12\x10\n\x0c\x44TYPE_STRING\x10\x08\x32\xb5\x01\n\x0c\x42\x65ntoService\x12=\n\x04\x43\x61ll\x12\x18.bentoml.grpc.v1.Request\x1a\x19.bentoml.grpc.v1.Response\"\x00\x12\x66\n\x0fServiceMetadata\x12\'.bentoml.grpc.v1.ServiceMetadataRequest\x1a(.bentoml.grpc.v1.ServiceMetadataResponse\"\x00\x42]\n\x13\x63om.bentoml.grpc.v1B\x0cServiceProtoP\x01Z*github.com/bentoml/bentoml/grpc/v1;service\x90\x01\x01\xf8\x01\x01\xa2\x02\x03SVCb\x06proto3')



_SERVICEMETADATAREQUEST = DESCRIPTOR.message_types_by_name['ServiceMetadataRequest']
_SERVICEMETADATARESPONSE = DESCRIPTOR.message_types_by_name['ServiceMetadataResponse']
_SERVICEMETADATARESPONSE_DESCRIPTORMETADATA = _SERVICEMETADATARESPONSE.nested_types_by_name['DescriptorMetadata']
_SERVICEMETADATARESPONSE_INFERENCEAPI = _SERVICEMETADATARESPONSE.nested_types_by_name['InferenceAPI']
_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
_PART = DESCRIPTOR.message_types_by_name['Part']
_MULTIPART = DESCRIPTOR.message_types_by_name['Multipart']
_MULTIPART_FIELDSENTRY = _MULTIPART.nested_types_by_name['FieldsEntry']
_FILE = DESCRIPTOR.message_types_by_name['File']
_DATAFRAME = DESCRIPTOR.message_types_by_name['DataFrame']
_SERIES = DESCRIPTOR.message_types_by_name['Series']
_NDARRAY = DESCRIPTOR.message_types_by_name['NDArray']
_NDARRAY_DTYPE = _NDARRAY.enum_types_by_name['DType']
ServiceMetadataRequest = _reflection.GeneratedProtocolMessageType('ServiceMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEMETADATAREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.grpc.v1.ServiceMetadataRequest)
  })
_sym_db.RegisterMessage(ServiceMetadataRequest)

ServiceMetadataResponse = _reflection.GeneratedProtocolMessageType('ServiceMetadataResponse', (_message.Message,), {

  'DescriptorMetadata' : _reflection.GeneratedProtocolMessageType('DescriptorMetadata', (_message.Message,), {
    'DESCRIPTOR' : _SERVICEMETADATARESPONSE_DESCRIPTORMETADATA,
    '__module__' : 'service_pb2'
    # @@protoc_insertion_point(class_scope:bentoml.grpc.v1.ServiceMetadataResponse.DescriptorMetadata)
    })
  ,

  'InferenceAPI' : _reflection.GeneratedProtocolMessageType('InferenceAPI', (_message.Message,), {
    'DESCRIPTOR' : _SERVICEMETADATARESPONSE_INFERENCEAPI,
    '__module__' : 'service_pb2'
    # @@protoc_insertion_point(class_scope:bentoml.grpc.v1.ServiceMetadataResponse.InferenceAPI)
    })
  ,
  'DESCRIPTOR' : _SERVICEMETADATARESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.grpc.v1.ServiceMetadataResponse)
  })
_sym_db.RegisterMessage(ServiceMetadataResponse)
_sym_db.RegisterMessage(ServiceMetadataResponse.DescriptorMetadata)
_sym_db.RegisterMessage(ServiceMetadataResponse.InferenceAPI)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.grpc.v1.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.grpc.v1.Response)
  })
_sym_db.RegisterMessage(Response)

Part = _reflection.GeneratedProtocolMessageType('Part', (_message.Message,), {
  'DESCRIPTOR' : _PART,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.grpc.v1.Part)
  })
_sym_db.RegisterMessage(Part)

Multipart = _reflection.GeneratedProtocolMessageType('Multipart', (_message.Message,), {

  'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _MULTIPART_FIELDSENTRY,
    '__module__' : 'service_pb2'
    # @@protoc_insertion_point(class_scope:bentoml.grpc.v1.Multipart.FieldsEntry)
    })
  ,
  'DESCRIPTOR' : _MULTIPART,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.grpc.v1.Multipart)
  })
_sym_db.RegisterMessage(Multipart)
_sym_db.RegisterMessage(Multipart.FieldsEntry)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.grpc.v1.File)
  })
_sym_db.RegisterMessage(File)

DataFrame = _reflection.GeneratedProtocolMessageType('DataFrame', (_message.Message,), {
  'DESCRIPTOR' : _DATAFRAME,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.grpc.v1.DataFrame)
  })
_sym_db.RegisterMessage(DataFrame)

Series = _reflection.GeneratedProtocolMessageType('Series', (_message.Message,), {
  'DESCRIPTOR' : _SERIES,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.grpc.v1.Series)
  })
_sym_db.RegisterMessage(Series)

NDArray = _reflection.GeneratedProtocolMessageType('NDArray', (_message.Message,), {
  'DESCRIPTOR' : _NDARRAY,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.grpc.v1.NDArray)
  })
_sym_db.RegisterMessage(NDArray)

_BENTOSERVICE = DESCRIPTOR.services_by_name['BentoService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.bentoml.grpc.v1B\014ServiceProtoP\001Z*github.com/bentoml/bentoml/grpc/v1;service\220\001\001\370\001\001\242\002\003SVC'
  _MULTIPART_FIELDSENTRY._options = None
  _MULTIPART_FIELDSENTRY._serialized_options = b'8\001'
  _SERIES.fields_by_name['bool_values']._options = None
  _SERIES.fields_by_name['bool_values']._serialized_options = b'\020\001'
  _SERIES.fields_by_name['float_values']._options = None
  _SERIES.fields_by_name['float_values']._serialized_options = b'\020\001'
  _SERIES.fields_by_name['int32_values']._options = None
  _SERIES.fields_by_name['int32_values']._serialized_options = b'\020\001'
  _SERIES.fields_by_name['int64_values']._options = None
  _SERIES.fields_by_name['int64_values']._serialized_options = b'\020\001'
  _SERIES.fields_by_name['double_values']._options = None
  _SERIES.fields_by_name['double_values']._serialized_options = b'\020\001'
  _NDARRAY.fields_by_name['float_values']._options = None
  _NDARRAY.fields_by_name['float_values']._serialized_options = b'\020\001'
  _NDARRAY.fields_by_name['double_values']._options = None
  _NDARRAY.fields_by_name['double_values']._serialized_options = b'\020\001'
  _NDARRAY.fields_by_name['bool_values']._options = None
  _NDARRAY.fields_by_name['bool_values']._serialized_options = b'\020\001'
  _NDARRAY.fields_by_name['int32_values']._options = None
  _NDARRAY.fields_by_name['int32_values']._serialized_options = b'\020\001'
  _NDARRAY.fields_by_name['int64_values']._options = None
  _NDARRAY.fields_by_name['int64_values']._serialized_options = b'\020\001'
  _NDARRAY.fields_by_name['uint32_values']._options = None
  _NDARRAY.fields_by_name['uint32_values']._serialized_options = b'\020\001'
  _NDARRAY.fields_by_name['uint64_values']._options = None
  _NDARRAY.fields_by_name['uint64_values']._serialized_options = b'\020\001'
  _SERVICEMETADATAREQUEST._serialized_start=96
  _SERVICEMETADATAREQUEST._serialized_end=120
  _SERVICEMETADATARESPONSE._serialized_start=123
  _SERVICEMETADATARESPONSE._serialized_end=601
  _SERVICEMETADATARESPONSE_DESCRIPTORMETADATA._serialized_start=247
  _SERVICEMETADATARESPONSE_DESCRIPTORMETADATA._serialized_end=358
  _SERVICEMETADATARESPONSE_INFERENCEAPI._serialized_start=361
  _SERVICEMETADATARESPONSE_INFERENCEAPI._serialized_end=601
  _REQUEST._serialized_start=604
  _REQUEST._serialized_end=993
  _RESPONSE._serialized_start=996
  _RESPONSE._serialized_end=1368
  _PART._serialized_start=1371
  _PART._serialized_end=1697
  _MULTIPART._serialized_start=1700
  _MULTIPART._serialized_end=1837
  _MULTIPART_FIELDSENTRY._serialized_start=1769
  _MULTIPART_FIELDSENTRY._serialized_end=1837
  _FILE._serialized_start=1839
  _FILE._serialized_end=1890
  _DATAFRAME._serialized_start=1892
  _DATAFRAME._serialized_end=1967
  _SERIES._serialized_start=1970
  _SERIES._serialized_end=2131
  _NDARRAY._serialized_start=2134
  _NDARRAY._serialized_end=2584
  _NDARRAY_DTYPE._serialized_start=2415
  _NDARRAY_DTYPE._serialized_end=2584
  _BENTOSERVICE._serialized_start=2587
  _BENTOSERVICE._serialized_end=2768
BentoService = service_reflection.GeneratedServiceType('BentoService', (_service.Service,), dict(
  DESCRIPTOR = _BENTOSERVICE,
  __module__ = 'service_pb2'
  ))

BentoService_Stub = service_reflection.GeneratedServiceStubType('BentoService_Stub', (BentoService,), dict(
  DESCRIPTOR = _BENTOSERVICE,
  __module__ = 'service_pb2'
  ))


# @@protoc_insertion_point(module_scope)