# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from config_routing.grpc import config_routing_pb2 as config__routing_dot_grpc_dot_config__routing__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class UserControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/config_routing.UserController/List',
                request_serializer=config__routing_dot_grpc_dot_config__routing__pb2.UserListRequest.SerializeToString,
                response_deserializer=config__routing_dot_grpc_dot_config__routing__pb2.UserListResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/config_routing.UserController/Create',
                request_serializer=config__routing_dot_grpc_dot_config__routing__pb2.User.SerializeToString,
                response_deserializer=config__routing_dot_grpc_dot_config__routing__pb2.User.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/config_routing.UserController/Retrieve',
                request_serializer=config__routing_dot_grpc_dot_config__routing__pb2.UserRetrieveRequest.SerializeToString,
                response_deserializer=config__routing_dot_grpc_dot_config__routing__pb2.User.FromString,
                )
        self.Update = channel.unary_unary(
                '/config_routing.UserController/Update',
                request_serializer=config__routing_dot_grpc_dot_config__routing__pb2.User.SerializeToString,
                response_deserializer=config__routing_dot_grpc_dot_config__routing__pb2.User.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/config_routing.UserController/Destroy',
                request_serializer=config__routing_dot_grpc_dot_config__routing__pb2.User.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class UserControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=config__routing_dot_grpc_dot_config__routing__pb2.UserListRequest.FromString,
                    response_serializer=config__routing_dot_grpc_dot_config__routing__pb2.UserListResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=config__routing_dot_grpc_dot_config__routing__pb2.User.FromString,
                    response_serializer=config__routing_dot_grpc_dot_config__routing__pb2.User.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=config__routing_dot_grpc_dot_config__routing__pb2.UserRetrieveRequest.FromString,
                    response_serializer=config__routing_dot_grpc_dot_config__routing__pb2.User.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=config__routing_dot_grpc_dot_config__routing__pb2.User.FromString,
                    response_serializer=config__routing_dot_grpc_dot_config__routing__pb2.User.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=config__routing_dot_grpc_dot_config__routing__pb2.User.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'config_routing.UserController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config_routing.UserController/List',
            config__routing_dot_grpc_dot_config__routing__pb2.UserListRequest.SerializeToString,
            config__routing_dot_grpc_dot_config__routing__pb2.UserListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config_routing.UserController/Create',
            config__routing_dot_grpc_dot_config__routing__pb2.User.SerializeToString,
            config__routing_dot_grpc_dot_config__routing__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config_routing.UserController/Retrieve',
            config__routing_dot_grpc_dot_config__routing__pb2.UserRetrieveRequest.SerializeToString,
            config__routing_dot_grpc_dot_config__routing__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config_routing.UserController/Update',
            config__routing_dot_grpc_dot_config__routing__pb2.User.SerializeToString,
            config__routing_dot_grpc_dot_config__routing__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config_routing.UserController/Destroy',
            config__routing_dot_grpc_dot_config__routing__pb2.User.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
