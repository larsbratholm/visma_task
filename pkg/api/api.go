package api

import (
	"context"
	"fmt"
	api "github.com/larsbratholm/visma_task/proto"
	"google.golang.org/grpc"
)

// Server is a server implementing the proto API
type Server struct{
    Client api.ImageScalerClient
}


// ScaleImage connects locally to python service
func (s *Server) ScaleImage(ctx context.Context, req *api.ScaleImageRequest) (
	*api.ScaleImageReply, error) {
	// Echo
	fmt.Println("Received image...")
	// Forward to python server
    reply, err := s.Client.ScaleImage(ctx, req)
    return reply, err
}

// Get connection to the python ImageScaler server
func GetImageScalerConnection(host string) (*grpc.ClientConn, error) {
    return grpc.Dial(host, grpc.WithInsecure())
}

