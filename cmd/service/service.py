""" Server for image pre-processing
"""

import grpc
import sys
import os
#import logging
import time
from concurrent import futures
from io import BytesIO
from PIL import Image

# Add the protobuf api to system path and import
sys.path.append(os.path.join(os.path.dirname(__file__), "../..", "proto"))
import api_pb2
import api_pb2_grpc

class ImageScaler(api_pb2_grpc.ImageScalerServicer):
    def ScaleImage(self, req, ctx):
        """ obtain re-scaled and possibly grey scaled images
        """
        content = req.image.content
        scaled_content = self._apply_scaling(content, req.resize, req.greyscaling)
        return api_pb2.ScaleImageReply(content=scaled_content)

    def _apply_scaling(self, content, resize, greyscaling):
        """ Do the actual preprocessing
        """
        img = self._bytes_to_image(content)
        img_format = img.format
        if greyscaling:
            img = self._convert_to_greyscale(img)

        if resize:
            img = img

        return self._image_to_bytes(img, fmt=img_format)

    def _convert_to_greyscale(self, img):
        """ Converts a PIL Image to greyscale
        """
        return img.convert("L")

    def _bytes_to_image(self, content):
        """ Convert the bytes stream to a PIL Image
        """
        bytes_io = BytesIO(content)
        return Image.open(bytes_io)

    def _image_to_bytes(self, image, fmt):
        """ Convert PIL Image to bytes stream
        """
        bytes_io = BytesIO()
        image.save(bytes_io, format=fmt)
        return bytes_io.getvalue()



if __name__ == "__main__":
    port = sys.argv[1] if len(sys.argv) > 1 else "50052"
    host = f"[::]:{port}"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    server.add_insecure_port(host)
    api_pb2_grpc.add_ImageScalerServicer_to_server(ImageScaler(), server)
    try:
        server.start()
        print("Running ImageScaler service on port %s" % port)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)

