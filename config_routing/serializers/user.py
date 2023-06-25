from config_routing.models import User
from django_socio_grpc import proto_serializers
from config_routing.grpc import config_routing_pb2

class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = config_routing_pb2.User # Modification here
        proto_class_list = config_routing_pb2.UserListResponse # Modification here
        fields = '__all__'
       
