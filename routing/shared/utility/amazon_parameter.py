import boto3
import ast


class AwsSystemManager():
    def __init__(self):
        self.ssm_client = boto3.client(
            service_name='ssm',
            region_name='us-east-1',
        )

    def get_ssm_key_data(self, parameter_name=None):
        response = self.ssm_client.get_parameter(
            Name=parameter_name, WithDecryption=True)
        print('Loading -- ' + response['Parameter']['Name'])
        json_data = ast.literal_eval(response['Parameter']['Value'])
        return json_data
