import grpc
from config_routing.grpc import config_routing_pb2
from config_routing.grpc import config_routing_pb2_grpc
from google.protobuf.json_format import MessageToDict
from google.protobuf import wrappers_pb2
from config_routing.shared.utility.logging import Logger


# channel_creds = grpc.ssl_channel_credentials()
# channel = grpc.secure_channel('localhost:50051', channel_creds)
channel = grpc.insecure_channel('localhost:50051')
print(channel)

# for getting the list 
stub = config_routing_pb2_grpc.UserControllerStub(channel)

def fetch_data():
    # for getting the list 
    try:
        array = []
        try:
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
        return array
        # convert_dict = MessageToDict(descriptor_pool=True, message=user.results)
    except Exception as e:
            return str(e)
x = fetch_data()
print("***")
print(x, end='')
print(type(x))
# data = MessageToDict(x)
# print(data, "datatttttt")

# for create the data 
response = stub.Create(config_routing_pb2.User(id= 6,name = "iuhuhu",email = "tej@gmail.com", groups = "carss" ))
print(response)

# a = config_routing_pb2.User(id= 3,name = "finallllll",email = "pkk@gmail.com", groups = "pop" )
# print(a, "aaaa")
# stub.Update(a)


# for delete 
# a = stub.Destroy(config_routing_pb2.User(id=3))
# print(a)

# retrieve on the basis of the id 
a =config_routing_pb2.UserRetrieveRequest(id = 3)
print(a)
response= stub.Retrieve(a)
print(response)


