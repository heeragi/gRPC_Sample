import grpc

import hello_pb2
import hello_pb2_grpc


def run():
    # channel connection
    with grpc.insecure_channel('localhost:8001') as channel:
        # client stub를 이용하여 채널 마샬링
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(data='jeong_ju_young', status_code=200))
        print(f'Greeter client received ${response.result}')
        print(f'Greeter client received ${response.status_code}')


if __name__ == '__main__':
    run()