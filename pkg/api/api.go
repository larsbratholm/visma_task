package api

import (
	"context"
	"fmt"
	api "github.com/larsbratholm/visma_task/proto"
)

// Server is a server implementing the proto API
//type Server struct{client *api.ImageScalerClient}
type Server struct{}

// ScaleImage connects locally to python service
func (s *Server) ScaleImage(ctx context.Context, req *api.ScaleImageRequest) (
	*api.ScaleImageReply, error) {
	// Echo
	fmt.Println("Received image...")
	return &api.ScaleImageReply{
		Content: req.Image.GetContent(),
	}, nil
	
//	return &api.ScaleImageReply{
//		Content: s.client.ScaleImage(ctx, req),
//	}, nil
}

//// Get connection to the python ImageScaler server
//func getImageScalerConnection(host string) (*grpc.ClientConn, error) {
//    return grpc.Dial(host, grpc.WithInsecure())
//}
//
//func getImageScalerClient(host string) *pb.ImageScalerClient{
//	conn, err := getImageScalerConnection(host)
//	if err != nil {
//		log.Fatalf("Did not connect to Image Scaler Client: %v", err)
//	}
//	defer conn.Close()
//
//	return pb.NewImageScalerClient(conn)
//}
