package main

import (
	"context"
	"io/ioutil"
	"log"

	pb "github.com/larsbratholm/visma_task/proto"
	"google.golang.org/grpc"
)

const (
	host = ":50051"
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
			Content: image,
            //Source: &pb.ImageSource{
            //    HttpUri: "https://miro.medium.com/max/1200/1*mk1-6aYaf_Bes1E3Imhc0A.jpeg",
            //},
		},
        Resize: true,
        AllowCrop: true,
        Greyscaling: true,
	})

	ioutil.WriteFile("out.jpg", resp.GetContent(), 0644)
}
