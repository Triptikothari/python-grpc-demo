from django_socio_grpc import tests
from django.contrib.auth.models import User
from config_routing.grpc import config_routing_pb2
from config_routing.grpc import config_routing_pb2_grpc
import grpc

class UserServiceTest():
    def __init__(self) -> None:
        self.channel = grpc.insecure_channel('localhost:50051')
    
    grpc.UnaryUnaryClientInterceptor()
    def test_create_user(self):
        stub = config_routing_pb2_grpc.UserControllerStub(self.channel)
        response = stub.Create(config_routing_pb2.User(username='tom', email='tom@account.com'))
        self.assertEqual(response.username, 'tom')
        self.assertEqual(response.email, 'tom@account.com')
        self.assertEqual(User.objects.count(), 1)
    

