package main

import (
	"log"
	"net"
	"net/http"
	"github.com/larsbratholm/visma_task/pkg/api"
	pb "github.com/larsbratholm/visma_task/proto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"google.golang.org/grpc"

	health "github.com/e-conomic/hiring-assigments/machinelearningteam/image-scaling-service/pkg/health/v1"
	api_health "google.golang.org/grpc/health/grpc_health_v1"
)

const (
	port = ":50051"
    image_scaler_host = ":50052"
)

// starts the Prometheus stats endpoint server
func startPromHTTPServer(port string) {
	http.Handle("/metrics", promhttp.Handler())
	if err := http.ListenAndServe(":"+port, nil); err != nil {
		log.Println("prometheus err", port)
	}
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	go startPromHTTPServer("5001")

	s := grpc.NewServer()

	// Register: Health
	healthServ := health.NewHealthCheckService()
	api_health.RegisterHealthServer(s, healthServ)

	// Register: ImageScalerServer (forward to python server)
    conn, err := api.GetImageScalerConnection(image_scaler_host)
    if err != nil {
      log.Fatalf("Did not connect to Image Scaler Client: %v", err)
    }
    defer conn.Close()

    client := pb.NewImageScalerClient(conn)
    pb.RegisterImageScalerServer(s, &api.Server{Client:client})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
