# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='imagescaler',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tapi.proto\x12\x0bimagescaler\"[\n\x11ScaleImageRequest\x12!\n\x05image\x18\x01 \x01(\x0b\x32\x12.imagescaler.Image\x12\x0e\n\x06resize\x18\x02 \x01(\x08\x12\x13\n\x0bgreyscaling\x18\x03 \x01(\x08\"\"\n\x0fScaleImageReply\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"B\n\x05Image\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12(\n\x06source\x18\x02 \x01(\x0b\x32\x18.imagescaler.ImageSource\"\x1f\n\x0bImageSource\x12\x10\n\x08http_uri\x18\x01 \x01(\t2[\n\x0bImageScaler\x12L\n\nScaleImage\x12\x1e.imagescaler.ScaleImageRequest\x1a\x1c.imagescaler.ScaleImageReply\"\x00\x62\x06proto3')
)




_SCALEIMAGEREQUEST = _descriptor.Descriptor(
  name='ScaleImageRequest',
  full_name='imagescaler.ScaleImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='imagescaler.ScaleImageRequest.image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resize', full_name='imagescaler.ScaleImageRequest.resize', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='greyscaling', full_name='imagescaler.ScaleImageRequest.greyscaling', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=117,
)


_SCALEIMAGEREPLY = _descriptor.Descriptor(
  name='ScaleImageReply',
  full_name='imagescaler.ScaleImageReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='imagescaler.ScaleImageReply.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=153,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='imagescaler.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='imagescaler.Image.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='imagescaler.Image.source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=221,
)


_IMAGESOURCE = _descriptor.Descriptor(
  name='ImageSource',
  full_name='imagescaler.ImageSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='http_uri', full_name='imagescaler.ImageSource.http_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=254,
)

_SCALEIMAGEREQUEST.fields_by_name['image'].message_type = _IMAGE
_IMAGE.fields_by_name['source'].message_type = _IMAGESOURCE
DESCRIPTOR.message_types_by_name['ScaleImageRequest'] = _SCALEIMAGEREQUEST
DESCRIPTOR.message_types_by_name['ScaleImageReply'] = _SCALEIMAGEREPLY
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['ImageSource'] = _IMAGESOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScaleImageRequest = _reflection.GeneratedProtocolMessageType('ScaleImageRequest', (_message.Message,), dict(
  DESCRIPTOR = _SCALEIMAGEREQUEST,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:imagescaler.ScaleImageRequest)
  ))
_sym_db.RegisterMessage(ScaleImageRequest)

ScaleImageReply = _reflection.GeneratedProtocolMessageType('ScaleImageReply', (_message.Message,), dict(
  DESCRIPTOR = _SCALEIMAGEREPLY,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:imagescaler.ScaleImageReply)
  ))
_sym_db.RegisterMessage(ScaleImageReply)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), dict(
  DESCRIPTOR = _IMAGE,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:imagescaler.Image)
  ))
_sym_db.RegisterMessage(Image)

ImageSource = _reflection.GeneratedProtocolMessageType('ImageSource', (_message.Message,), dict(
  DESCRIPTOR = _IMAGESOURCE,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:imagescaler.ImageSource)
  ))
_sym_db.RegisterMessage(ImageSource)



_IMAGESCALER = _descriptor.ServiceDescriptor(
  name='ImageScaler',
  full_name='imagescaler.ImageScaler',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=256,
  serialized_end=347,
  methods=[
  _descriptor.MethodDescriptor(
    name='ScaleImage',
    full_name='imagescaler.ImageScaler.ScaleImage',
    index=0,
    containing_service=None,
    input_type=_SCALEIMAGEREQUEST,
    output_type=_SCALEIMAGEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGESCALER)

DESCRIPTOR.services_by_name['ImageScaler'] = _IMAGESCALER

# @@protoc_insertion_point(module_scope)
