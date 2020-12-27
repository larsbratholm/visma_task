package api

import (
	"context"
	"fmt"

	api "github.com/larsbratholm/visma_task/proto"
)

// Server is a server implementing the proto API
type Server struct{}

// ScaleImage echoes the image provides in the request
func (s *Server) ScaleImage(ctx context.Context, req *api.ScaleImageRequest) (
	*api.ScaleImageReply, error) {
	// Echo
	fmt.Println("Received image...")
	return &api.ScaleImageReply{
		Content: req.Image.GetContent(),
	}, nil
}
