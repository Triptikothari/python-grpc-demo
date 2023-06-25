# import grpc
# from config_routing.models import PebMerchantInfo, PebSubMerchantInfo
# from django_socio_grpc import generics
# from google.protobuf import empty_pb2
# from google.protobuf.json_format import MessageToDict
# from config_routing.serializers.pebmerchantinfo import PebMerchantProtoSerializer
# from config_routing.serializers.pebsubmerchantinfo import PebSubMerchantInfoProtoSerializer


# #all the crud operations 


# class InitiateLinkController(generics.AsyncModelService):
#     """
#     gRPC service that allows users to be retrieved or updated.
#     """
#     def get_object(self, pk):
#         try:
#             return PebMerchantInfo.objects.get(pk=pk)
#         except PebMerchantInfo.DoesNotExist:
#             self.context.abort(grpc.StatusCode.NOT_FOUND, 'Post:%s not found!' % pk)
#     def FetchMerchantData(self, request, context):
#         print("uuuuuuuuuuuuuuuuuuuuuuu")
#         print(request.submerchant_id)
#         print(request.merchant_id, "ssssss")
#         try:
#             merchant_data = PebMerchantInfo.objects.select_related("merchant_settings", "gateway_settings").get(pk=request.merchant_id)
#         except PebMerchantInfo.DoesNotExist:
#             self.context.abort(grpc.StatusCode.NOT_FOUND, 'Post:%s not found!' % merchant_data)
#         merchant_serializer_class = PebMerchantProtoSerializer(merchant_data)
#         try:
#             if request.submerchant_id:
#                 submerchant_data = PebSubMerchantInfo.objects.select_related("gateway_settings").get(merchant=request.merchant_id,  pk=request.submerchant_id)
#                 serializer_class = PebSubMerchantInfoProtoSerializer(submerchant_data)
#                 print(serializer_class)
#             else:
#                 serializer_class = ""
#         except PebSubMerchantInfo.DoesNotExist:
#             self.context.grpc_context(grpc.StatusCode.NOT_FOUND, 'Post:%s not found!' % request.submerchant_id)
#         # response_data['message']={
#         #         'agent_info': merchant_serializer_class.message,
#         #         'team_info': serializer_class.message
#         #     }    
#         return merchant_serializer_class.message
    

#     def FetchSubMerchantData(self, request, context):
#         print("uuuuuuuuuuuuuuuuuuuuuuu")
#         print(request.submerchant_id)
#         print(request.merchant_id, "ssssss")
#         try:
#             if request.submerchant_id:
#                 submerchant_data = PebSubMerchantInfo.objects.select_related("gateway_settings").get(merchant=request.merchant_id,  pk=request.submerchant_id)
#                 serializer_class = PebSubMerchantInfoProtoSerializer(submerchant_data)
#                 print(serializer_class)
#                 return serializer_class.message
#             else:
#                 return empty_pb2.Empty()
#         except PebSubMerchantInfo.DoesNotExist:
#             self.context.grpc_context(grpc.StatusCode.NOT_FOUND, 'Post:%s not found!' % request.submerchant_id)
#         # response_data['message']={
#         #         'agent_info': merchant_serializer_class.message,
#         #         'team_info': serializer_class.message
#         #     }
        


    