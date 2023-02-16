import concurrent.futures
import grpc
import hello_pb2
import hello_pb2_grpc


class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(result=f'Hello ${request.data}', status_code=200)


def serve():
    # grpc server 생성
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    # grpc server 에 서비스 등록
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    # grpc server 웹서버 생성
    server.add_insecure_port('localhost:8001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
