import sys
sys.path.append('./pb')

from urllib.request import urlopen
import grpc
import time
import face_recognition
from pb import face_pb2, face_pb2_grpc
from concurrent import futures

class FaceService(face_pb2_grpc.FaceRecognitionServicer):
  def IsFaceBeauty(self, request, context):
      image = face_recognition.load_image_file(urlopen(request.src))
      locations = face_recognition.face_locations(image)
      result = True if len(locations) > 0 and len(locations) < 3 else False
      return face_pb2.IsFaceBeautyReply(result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    face_pb2_grpc.add_FaceRecognitionServicer_to_server(FaceService(), server)
    server.add_insecure_port('[::]:51111')
    server.start()
    try:
        while True:
            # 一个月
            time.sleep(60 * 60 * 24 * 31)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
