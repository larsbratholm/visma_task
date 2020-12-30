package main

import (
	"context"
	"io/ioutil"
	"log"
	"fmt"

	pb "github.com/larsbratholm/visma_task/proto"
	"google.golang.org/grpc"
)

const (
	host = "localhost:50051"
)

func main() {
	conn, err := grpc.Dial(host, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	client := pb.NewImageScalerClient(conn)

	image, err := ioutil.ReadFile("test.jpg")
	if err != nil {
		log.Fatal("Couldn't read input image")
	}
	ctx := context.Background()
	resp, err := client.ScaleImage(ctx, &pb.ScaleImageRequest{
		Image: &pb.Image{
			Content: image,
		},
//        Rescale: false,
//        Greyscaling: false,
	})

	ioutil.WriteFile("out.jpg", resp.GetContent(), 0644)
}
