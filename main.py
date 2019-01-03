import pb
import grpc
from concurrent import futures

class FaceService(pb.face_pb2_grpc.FaceRecognitionServicer):
  def IsFaceBeauty(self, request, context):
      return pb.face_pb2.IsFaceBeautyReply(True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb.face_pb2_grpc.add_FaceRecognitionServicer_to_server(FaceService(), server)
    server.add_insecure_port('[::]:51111')
    server.start()

if __name__ == '__main__':
    serve()