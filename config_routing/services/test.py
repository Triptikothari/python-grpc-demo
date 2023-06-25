import grpc
from config_routing.grpc import config_routing_pb2
from config_routing.grpc import config_routing_pb2_grpc
from google.protobuf.json_format import MessageToDict
import json
from config_routing.shared.utility.logging import Logger



class TestService():
    def __init__(self) -> None:
        self.channel = grpc.insecure_channel('localhost:50051')

    def fetch_data(self):
        # for getting the list 
        try:
            array = []
            try:
                stub = config_routing_pb2_grpc.UserControllerStub(self.channel)
                user = stub.List(config_routing_pb2.UserListRequest())
            except grpc.RpcError as e:
                Logger.exception('Exception Occurred GRPC Server Error- {}'.format(str(e)))
                return{'status' : 400, 'message' : "grpc server error"}
            # print(grpc.StatusCode)
            # import pdb
            # pdb.set_trace()
            # print(MessageToDict(user))
            # convert_dict = MessageToDict(user)
            # print(convert_dict["result"], "tttttttttttt")
            for x in user.results:
                array.append({
                    'id' :x.id,
                    'name' : x.name,
                    'email' : x.email,
                    'groups' : x.groups
                })
            return {'status': 200, 'data': array}
            # convert_dict = MessageToDict(descriptor_pool=True, message=user.results)
        except Exception as e:
            return{'status': 400, 'message': str(e)}