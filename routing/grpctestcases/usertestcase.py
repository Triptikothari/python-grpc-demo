from django_socio_grpc import tests
from django.contrib.auth.models import User
from routing.grpc import routing_pb2
from routing.grpc import routing_pb2_grpc
import grpc

class UserServiceTest():
    def __init__(self) -> None:
        self.channel = grpc.insecure_channel('localhost:50051')
    
    grpc.UnaryUnaryClientInterceptor()
    def test_create_user(self):
        stub = routing_pb2_grpc.UserControllerStub(self.channel)
        response = stub.Create(routing_pb2.User(username='tom', email='tom@account.com'))
        self.assertEqual(response.username, 'tom')
        self.assertEqual(response.email, 'tom@account.com')
        self.assertEqual(User.objects.count(), 1)
    

