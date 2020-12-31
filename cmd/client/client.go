package main

import (
	"context"
	"io/ioutil"
	"log"

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
	_ = image
	if err != nil {
		log.Fatal("Couldn't read input image")
	}
	ctx := context.Background()
	resp, err := client.ScaleImage(ctx, &pb.ScaleImageRequest{
		Image: &pb.Image{
			//Content: image,
            Source: &pb.ImageSource{
                HttpUri: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Conan_O%27Brien_by_Gage_Skidmore_2.jpg/1200px-Conan_O%27Brien_by_Gage_Skidmore_2.jpg",
            },
		},
        Resize: true,
        AllowCrop: true,
        Greyscaling: true,
	})

	ioutil.WriteFile("out.jpg", resp.GetContent(), 0644)
}
