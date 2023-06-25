from routing.grpccontrollers.user_controller import UserController
from django_socio_grpc.utils.servicer_register import AppHandlerRegistry
from routing.grpc import routing_pb2_grpc

#Every GRPC Controller should be added to the GRPC Handler
def grpc_handlers(server):
    # app_registry = AppHandlerRegistry("routing", server)
    # app_registry.register(User)
    routing_pb2_grpc.add_UserControllerServicer_to_server(UserController(), server)
