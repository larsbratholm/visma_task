import grpc

# import the generated classes
# Add the protobuf api to system path and import
sys.path.append(os.path.join(os.path.dirname(__file__), "../..", "proto"))
import api_pb2
import api_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = calculator_pb2.Number(value=16)

# make the call
response = stub.SquareRoot(number)

# et voilà
print(response.value)
