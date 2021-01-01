FROM golang:1.13 AS builder

WORKDIR /app


RUN wget -O grpc-health-probe -q https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/v0.3.1/grpc_health_probe-linux-amd64 \
    && chmod +x grpc-health-probe
COPY go.mod .
COPY go.sum .
RUN go mod download

COPY . .

# Build the application
RUN go build cmd/service/service.go

# Setup anaconda environment since grpcio takes forever to build via pip
FROM continuumio/miniconda3 AS conda

COPY environment.yml .
RUN conda env create -f environment.yml

FROM debian:stretch-slim AS runner

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates

COPY --from=builder /app/service /app/service
COPY --from=builder /app/grpc-health-probe /usr/local/bin/grpc-health-probe

COPY cmd/service/service.py .
COPY proto/api_pb2.py .
COPY proto/api_pb2_grpc.py .

COPY --from=conda /opt/conda /opt/conda
ENV PATH=/opt/conda/bin:$PATH

EXPOSE 50051
# sleep to make sure python server is up and running before go server
ENTRYPOINT ["conda", "run", "-n", "imagescaler", "python", "/app/service.py", "&", "sleep 4", "&", "/app/service"]
