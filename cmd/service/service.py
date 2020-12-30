""" Server for image pre-processing
"""

import grpc
import sys
import os
#import logging
import time
from concurrent import futures

# Add the protobuf api to system path and import
sys.path.append(os.path.join(os.path.dirname(__file__), "../..", "proto"))
import api_pb2
import api_pb2_grpc

class ImageScaler(api_pb2_grpc.ImageScalerServicer):
    def ScaleImage(self, req, ctx):
        """ obtain re-scaled and possibly grey scaled images
        """
        #scaled_content = self._apply_scaling(image.content)
        return api_pb2.ScaleImageReply(content=req.image.content)

    def _apply_scaling(self, content, rescale, greyscaling):
        """ Do the actual preprocessing
        """
        return content


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

