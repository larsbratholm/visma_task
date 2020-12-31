""" Server for image pre-processing
"""

import grpc
import sys
import os
import time
import requests
from concurrent import futures
from io import BytesIO
from PIL import Image
import numpy as np

# Add the protobuf api to system path and import
sys.path.append(os.path.join(os.path.dirname(__file__), "../..", "proto"))
import api_pb2
import api_pb2_grpc

class ImageScaler(api_pb2_grpc.ImageScalerServicer):
    def ScaleImage(self, req, ctx):
        """ obtain re-scaled and possibly grey scaled images
        """
        # If no bytes stream or url is sent, return empty content
        if len(req.image.content) == 0 and len(req.image.source.http_uri) == 0:
            print("Warning, no image content or URL sent")
            scaled_content = req.image.content
        else:
            img = self._get_image(req)
            scaled_content = self._apply_scaling(img, req)
        return api_pb2.ScaleImageReply(content=scaled_content)

    def _get_image(self, req):
        """ Extracts a PIL image either from bytes stream
            or URL
        """
        if len(req.image.content) > 0:
            content = req.image.content
        else:
            response = requests.get(req.image.source.http_uri)
            content = response.content

        bytes_io = BytesIO(content)
        return Image.open(bytes_io)

    def _apply_scaling(self, img, req):
        """ Do the actual preprocessing
        """
        img_format = img.format

        if req.resize:
            img = self._resize(img, req)
        # Grey scaling last as resizing might work better in colours
        if req.greyscaling:
            img = self._convert_to_greyscale(img)

        return self._image_to_bytes(img, fmt=img_format)

    def _resize(self, img, req):
        """ Handles all resizing of the PIL image
        """
        size = self._get_target_size(img, req)
        box = self._get_image_box(req, img, size)
        return img.resize(size=size,
                          box=box, resample=Image.LANCZOS)

    def _get_target_size(self, img, req):
        """ Infers the target image size
        """
        width, height = img.size
        # If only height or width is given
        # use those to set final dimensions
        if req.height == 0 and req.width > 0:
            out_width = req.width
            out_height = height * out_width / width
        elif req.height > 0 and req.width == 0:
            out_height = req.height
            out_width = width * out_height / height
        # If both are given, resize as normal
        elif req.height > 0 and req.width > 0:
            out_width, out_height = req.width, req.height
        else:
            # use 1024x768 as default
            out_width, out_height = (1024, 768)

        return (out_width, out_height)

    def _get_image_box(self, req, img, size):
        """ Creates a box defining the region of the image to be resized
        """
        width, height = img.size
        out_width, out_height = size
        ratio = (height / width) / (out_height / out_width)
        # if cropping is allowed, do a random crop if the
        # ratios differ by more than 5%
        if req.allow_crop and max(ratio, 1 / ratio) > 1.05:
            # Need to crop height
            if ratio > 1:
                aspect_ratio_height = int(out_height * width / out_width)
                upper = np.random.randint(0, height - aspect_ratio_height)
                lower = upper + aspect_ratio_height
                box = (0, upper, width, lower)
            # Need to crop width
            else:
                aspect_ratio_width = int(out_width * height / out_height)
                left = np.random.randint(0, width - aspect_ratio_width)
                right = left + aspect_ratio_width
                box = (left, 0, right, height)
        else:
            box = (0, 0, width, height)
        return box





    def _convert_to_greyscale(self, img):
        """ Converts a PIL Image to greyscale
        """
        print(54)
        return img.convert("L")

    def _image_to_bytes(self, image, fmt):
        """ Convert PIL Image to bytes stream
        """
        print(55)
        bytes_io = BytesIO()
        print(56)
        image.save(bytes_io, format=fmt)
        print(57)
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

