import grpc
from routing.models import User
from django_socio_grpc import generics
from routing.serializers.user import UserProtoSerializer
from google.protobuf import empty_pb2

#all the crud operations 


class UserController(generics.AsyncModelService):
    """
    gRPC service that allows users to be retrieved or updated.
    """
    # queryset = 
    # serializer_class = 

    

    def List(self, request, context):
        user = User.objects.all()
        serializer = UserProtoSerializer(user, many=True)
        print(serializer)
        return serializer.message

    def get_object(self, pk, context):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            context.abort(grpc.StatusCode.NOT_FOUND, 'Post:%s not found!')

    def Create(self, request, context):
        
        print(request)
        data = User.objects.filter(id = request.id)
        if data.exists():
            context.abort(grpc.StatusCode.ALREADY_EXISTS, 'id Already exist!')
        else :
            print(request, "ppppppppppppppppp")
            serializer_class = UserProtoSerializer(message=request)
            serializer_class.is_valid(raise_exception=True)
            serializer_class.save()
            return serializer_class.message
           
    
    def Retrieve(self, request, context):
        print(request.id)
        fetch_id = self.get_object(request.id, context)
        serializer_class = UserProtoSerializer(fetch_id)
        return serializer_class.message

    def Update(self, request, context):
        update_data = self.get_object(request.id, context)
        serializer_class = UserProtoSerializer(update_data, message=request)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return serializer_class.message

    def Destroy(self, request, context):
        print(request.id)
        delete_id = self.get_object(request.id)
        delete_id.delete()
        return empty_pb2.Empty()
    # # queryset = User.objects.all()
    # # serializer_class = UserProtoSerializer
    # # def List(self, request, context):
    # #     posts = User.objects.all()
    # #     serializer_class = UserProtoSerializer(posts, many=True)
    # #     for msg in serializer_class.message:
    # #         yield msg
    # # queryset = User.objects.all()
    # # serializer_class = UserProtoSerializer


    # def List(self, request, context):
    #     queryset = User.objects.first()
    #     print(queryset, "eeeeeeee")
    #     serializer_class = UserProtoSerializer(queryset, many=True)
    #     # print(serializer_class.message, "ppppppppppppppppp")
    #     for msg in serializer_class.message:
    #         yield msg
    #     # print(serializer_class, "mmmmmmmmm")
    #     # print(serializer_class.message_to_data, "ffffffffffffff")
    #     # print(serializer_class.message, "messsssss")
    #     # return serializer_class.message

    #     # return serializer_class.message
    #     # for msg in serializer_class:
    #     #     print("***")
    #     #     print(msg)
    #     #     yield msg
