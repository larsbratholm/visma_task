package api

import (
	"context"
	"fmt"

	api "github.com/e-conomic/hiring-assigments/machinelearningteam/image-scaling-service/proto"
)

// Server is a server implementing the proto API
type Server struct{}

// ScaleImage echoes the image provides in the request
func (s *Server) ScaleImage(ctx context.Context, req *api.ScaleImageRequest) (
	*api.ScaleImageReply, error) {
	// Echo
	fmt.Println("Recieved image...")
	return &api.ScaleImageReply{
		Content: req.Image.GetContent(),
	}, nil
}
