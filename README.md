# Preface
I didn't have any prior experience with Go, gRPC, docker or kubernetes, so a working docker image with an image scaling service is as far as I got.
There's a few hacks due to my lack of Go expertise:
- I edited [api.pb.go](./proto/api.pb.go) directly as the service couldn't compile with the auto-generated code from `protoc`, likely due to some missing flags or version differences.
- I forward requests from [service.go](./cmd/service/service.go) to the python server [service.py](./cmd/service/service.py) and I chose to connect to the client as part of [service.go](./cmd/service/service.go). Ideally this would be handled in [api.go](./pkg/api/api.go), but the only way I managed to get that working was to remake the connection for every request, and I opted for the former solution.
## Setup
Run
`python -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/api.proto`
to generate python source code for gRPC server interface.
This is symlinked in the python service folder.
## Details
The image will be processed from the bytes stream if available, else it will be read from a given URL.
If `Greyscaling: true` is given, the processed image will be grey-scaled. 
`Resize: true` with the options `Height`, `Width` and `AllowCrop` resizes the image using the following logic.

If only `Height` or `Width` are given, the other value will be set to keep the aspect ratio of the image.
If neither is given, 1024x768 will be used as default.
If the requested image ratio doesn't match the given image, the image will be squished or stretched during resizing, unless `AllowCrop: true` is given.
In that case, the same behavior is used if the requested aspect ratio is within a 5% margin of the given image.
Outside this margin, a random crop will be performed that keeps as much of the original image as possible.
