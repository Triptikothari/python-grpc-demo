from config_routing.grpccontrollers.user_controller import UserController
from django_socio_grpc.utils.servicer_register import AppHandlerRegistry
from config_routing.grpc import config_routing_pb2_grpc

#Every GRPC Controller should be added to the GRPC Handler
def grpc_handlers(server):
    # app_registry = AppHandlerRegistry("config_routing", server)
    # app_registry.register(User)
    config_routing_pb2_grpc.add_UserControllerServicer_to_server(UserController(), server)
