install requirements.txt

commands 
python manage.py runserver
python manage.py grpcrunserver --dev 
* To generate the Proto File 
    - python -m grpc_tools.protoc --proto_path=./ --python_out=./ --grpc_python_out=./ ./config_routing/grpc/(proto file path )
python client.py 