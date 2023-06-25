from routing.models import User
from django_socio_grpc import proto_serializers
from routing.grpc import routing_pb2

class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = routing_pb2.User # Modification here
        proto_class_list = routing_pb2.UserListResponse # Modification here
        fields = '__all__'
       
