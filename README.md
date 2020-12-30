# Description
Super hack due to since the auto generated code from protoc broke the service.
## Setup
Run
`python -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/api.proto`
and
`protoc -I=.. --go_out=./proto ./proto/api.proto`
to generate source code for gRPC server interface
