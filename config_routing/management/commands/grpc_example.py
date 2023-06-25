import traceback
from django.core.management.base import BaseCommand
from grpc_tools import protoc

class Command(BaseCommand):


    def handle(self, *args, **options):
        try:
        
            protoc.main(
                (
                    '-I',
                    '--python_out=./',   # go_out, js_out , java_out 
                    '--grpc_python_out=./',  # grpc_go_out, grpc_js_out , grpc_java_out 
                    './config_routing/grpc/config_routing.proto', #path of the proto file 
                )
            )
            # grpc_tools.protoc --proto_path=./ --python_out=./ --grpc_python_out=./ ./config_routing/grpc/config_routing.proto
            print("response")
        except Exception as e:
            traceback.print_exc()
            print({"response_status": False, "message": "Something went wrong, please try again"})