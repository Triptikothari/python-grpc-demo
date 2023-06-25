import json
import redis
import uuid
import boto3
import string
import random
import os
from django.conf import settings
from django_redis import get_redis_connection
from random import randint
from botocore.exceptions import ClientError

SqsUrl = ""

BOTO_ENV_DICTIONARY = {
    "prod": {
        "region": "ap-south-1",
        "profile_name": ""
    },
    "dev": {
        "region": "us-east-1",
        "profile_name": ""
    },
    "local": {
        "region": "us-east-1",
        "profile_name": "dev-sqs"
    },
    "local-dev": {
        "region": "us-east-1",
        "profile_name": "dev-sqs"
    }
}


class Push:

    def __init__(self):
        print("Initializing Push.py")
        self.app_env = settings.APP_ENV
        self.core_settings = self.__get_core_settings()
        try:
            if settings.APP_ENV == 'prod':
                if settings.QUEUE_APPLICATION == "redis":
                    self.cache = get_redis_connection("dakiya-prod")
                else:
                    self.sqs_client = boto3.client('sqs', 'ap-south-1')
                    self.SqsUrl = "https://sqs.ap-south-1.amazonaws.com/341444356059/"
            elif settings.APP_ENV == 'dev':
                self.sqs_client = boto3.client('sqs', 'ap-south-1')
                self.SqsUrl = "https://sqs.ap-south-1.amazonaws.com/684740219706/"
            else:
                self.session = boto3.Session(profile_name='dev-sqs')
                self.sqs_client = self.session.client('sqs')
                self.SqsUrl = "https://sqs.ap-south-1.amazonaws.com/684740219706/"
        except Exception as e:
            print(str(e))
            self.session = boto3.Session(profile_name='dev-sqs')
            self.sqs_client = self.session.client('sqs')
            self.SqsUrl = "https://sqs.ap-south-1.amazonaws.com/684740219706/"

    def __get_core_settings(self):
        boto_client = boto3.Session(profile_name=BOTO_ENV_DICTIONARY[self.app_env]["profile_name"]).client(
            'ssm') if self.app_env in ["local", "local-dev"] else boto3.client('ssm', BOTO_ENV_DICTIONARY[self.app_env]["region"])
        response = boto_client.get_parameter(
            Name="/Solutions/dakiya/config", WithDecryption=True)
        return json.loads(response["Parameter"]["Value"])

    def push_mail(self, subject, message, from_mail, recipient_list, priority=10, service_provider='bulk_aws_email',
                  cc_list=[], bcc_list=[], attachment={}, reply_to=[], config={}, application="", user=""):
        print("Pushpy.push_mail : Subject: " + subject)
        data = {
            'subject': subject,
            'message': message,
            'from': from_mail,
            'recipient_list': recipient_list,
            'cc_list': cc_list,
            'bcc_list': bcc_list,
            'reply_to': reply_to,
            'attachment': attachment,
            'status': 'pending'
        }
        response = self.__push_to_queue(
            priority, 'email', service_provider, data, config=config, application=application, user=user)
        return response

    def push_mass_mail(self, subject, message, html_message, from_mail, recipient_list, priority=10,
                       service_provider='aws_email', config={}, application="", user=""):
        print("Pushpy.push_mass_mail")
        data = {
            'subject': subject,
            'message': message,
            'html_message': html_message,
            'from': from_mail,
            'recipient_list': recipient_list,
            'status': 'pending'
        }
        response = self.__push_to_queue(
            priority, 'mass_email', service_provider, data, config=config, application=application, user=user)
        return response

    def push_sms(self, message, recipient_list, priority=10, service_provider='mvaayoo', config={}, application="", user="", template_id=""):
        print("Pushpy.push_sms : Message: ")
        if service_provider == 'aws_sns':
            recipient_list = self.__filter_phone_number(recipient_list)
        data = {
            'message': message,
            'recipient_list': recipient_list,
            'status': 'pending',
            'template_id': template_id
        }
        response = self.__push_to_queue(
            priority, 'sms', service_provider, data, config=config, application=application, user=user)
        return response

    def push_webhook(self, payload, priority=10, service_provider="", application="", user="", scheduler={}):
        data = {
            'payload': payload,
            'status': 'pending'
        }
        config = {}
        response = self.__push_to_queue(priority, 'webhook', service_provider, data,
                                        scheduler=scheduler, config=config, application=application, user=user)
        return response

    def push_whatsapp(self, message, recipient_list, priority=10, service_provider='clare', config={}, application="", user="", whatsapp_settings={}, sms_settings={}):
        print("Pushpy.push_whatsapp")
        if service_provider in ['clare', 'kaleyra']:
            recipient_list = self.__filter_phone_number(recipient_list)
        data = {
            'message': message,
            'recipient_list': recipient_list,
            'status': 'pending',
            'whatsapp_template': whatsapp_settings["whatsapp_template"],
            'message_name': whatsapp_settings["message_name"],
            'broadcast_name': whatsapp_settings.get("broadcast_name", ""),
            'dynamic_text': whatsapp_settings.get("dynamic_text", []),
            'dynamic_link': whatsapp_settings.get("dynamic_link", []),
            'dynamic_image_link': whatsapp_settings.get("dynamic_image_link", []),
            'sms_template_id': whatsapp_settings["sms_template_id"],
            'sms_setting': sms_settings
        }
        response = self.__push_to_queue(
            priority, 'whatsapp', service_provider, data, config=config, application=application, user=user)
        return response

    def push_obd_call(self, recipient_list, priority=10, service_provider='obd_call_virinchi', config={}, application="", user="", attachment={}, obd_call_settings={}):
        print("Pushpy.push_obd_call")
        data = {
            'recipient_list': recipient_list,
            'attachment': attachment,
            'status': 'pending'
        }
        data.update(obd_call_settings)
        response = self.__push_to_queue(
            priority, 'obd_call', service_provider, data, config=config, application=application, user=user)
        return response

    def push_obd_prompt_call(self, recipient_list, priority=10, service_provider='obd_prompt_call_virinchi', config={}, application="", user="", attachment={}):
        print("Pushpy.push_obd_prompt_call")
        data = {
            'recipient_list': recipient_list,
            'attachment': attachment,
            'status': 'pending'
        }
        response = self.__push_to_queue(
            priority, 'obd_prompt_call', service_provider, data, config=config, application=application, user=user)
        return response

    def __push_to_queue(self, priority, channel_type, service_provider, data, config, application, user, scheduler={}):
        try:
            print('----Push to Queue ---------')
            BASE_DIR = settings.BASE_DIR
            payload = {
                'priority': priority,
                'type': channel_type,
                'service_provider': service_provider,
                'user_id': user,
                'application': application,
                'data': data
            }
            if config:
                payload['config'] = config

            if scheduler:
                self.validate_scheduler_payload(scheduler)
                payload['scheduler'] = scheduler

            if channel_type in ['email', 'obd_call', 'obd_prompt_call']:
                if 'attachment_details' in payload['data']['attachment'].keys():
                    if len(payload['data']['attachment']['attachment_details']) > 0:
                        payload['data']['attachment'] = self.upload_to_s3(
                            data['attachment'], BASE_DIR)

            print('------------------')
            print("Payload: " + str(payload))
            print('------------------')

            if settings.QUEUE_APPLICATION == 'sqs':
                response = self.__push_to_sqs(payload)
            elif settings.QUEUE_APPLICATION == 'redis':
                response = self.__push_to_redis(payload)
            else:
                response = self.__push_to_sqs(payload)
            return response

        except Exception as e:
            print(str(e))

    def __push_to_redis(self, payload):
        print("Pushpy.__push_to_redis ")
        uuid_key = uuid.uuid1().int
        redis_cache_key = "dakiya_payload_" + str(uuid_key) + "_" + "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        check_exist = self.cache.get(redis_cache_key)
        if check_exist:
            uuid_key = uuid.uuid1().int
            redis_cache_key = "dakiya_payload_" + str(uuid_key) + "_" + "".join(
                random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        self.cache.set(redis_cache_key, json.dumps(payload))
        response = {'status': True, 'redis_cache_key': redis_cache_key}
        return response

    def __push_to_sqs(self, payload):
        try:
            print("Pushpy.__push_to_sqs ")
            queue_name = "dakiya_low_priority"

            if 1 <= payload['priority'] <= 10:
                queue_name = "dakiya_high_priority"
            elif 11 <= payload['priority'] <= 50:
                queue_name = "dakiya_medium_priority"
            SqsUrl = self.core_settings[self.app_env]["sqs_url"]
            QueueUrl = SqsUrl + queue_name
            response = self.sqs_client.send_message(
                QueueUrl=QueueUrl,
                MessageBody=json.dumps(payload))

            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                final_response = {'status': True, 'response': response}
            else:
                final_response = {'status': False}
        except ClientError as e:
            print(str(e))
            final_response = {'status': False}

        return final_response

    def __filter_phone_number(self, recipient_list):
        new_recipient_list = []

        for number in recipient_list:
            temp = number
            if len(number) < 11:
                temp = ''.join(('+91', temp))
            elif len(number) == 11:
                temp = temp[1:]
                temp = ''.join(('+91', temp))
            new_recipient_list.append(temp)
        return new_recipient_list

    def upload_to_s3(self, attachment_list, BASE_DIR):

        if settings.APP_ENV == 'local':
            session = boto3.Session(profile_name='dev-sqs')
            s3 = session.client('s3')
        else:
            s3 = boto3.client('s3')

        AWS_REGION = 'ap-south-1'

        if len(attachment_list['attachment_details']) > 0:
            upload_directory_path = settings.BASE_DIR + '/static/attachments/'
            if not os.path.exists(upload_directory_path):
                os.makedirs(upload_directory_path)
            for attachment in attachment_list['attachment_details']:
                aws_attachment_storage_bucket_name = "prod-dakiya" if settings.APP_ENV == "prod" else "dakiya-dev"
                aws_s3_attachment_domain = 's3.{0}.amazonaws.com/{1}'.format(AWS_REGION,
                                                                             aws_attachment_storage_bucket_name)
                s3_file_name = "".join(random.choice(string.ascii_uppercase + string.digits)
                                       for _ in range(5)) + "__" + attachment['filename']
                os.rename(attachment['url'],
                          upload_directory_path + s3_file_name)
                file_path = upload_directory_path + s3_file_name
                try:
                    s3.upload_file(file_path, aws_attachment_storage_bucket_name,
                                   attachment['folder_name'] + s3_file_name)
                    attachment_s3_path = 'https://{0}/{1}{2}'.format(aws_s3_attachment_domain,
                                                                     attachment['folder_name'], s3_file_name)
                    attachment['url'] = attachment_s3_path
                    attachment['uploaded_file_name'] = attachment['folder_name'] + s3_file_name
                    os.remove(file_path)
                except ClientError as s3e:
                    print(str(s3e))

        return attachment_list

    def push_notification(self, title, body, user_id_list, webhook_url, payload={}, priority=10, service_provider='google_fcm', config={}, application="", user=""):
        print("Pushpy.push_notification : Message: ")
        data = {
            'title': title,
            'body': body,
            'recipient_list': user_id_list,
            'status': 'pending',
            'webhook_url': webhook_url,
            'data': payload
        }
        response = self.__push_to_queue(
            priority, 'push_notification', service_provider, data, config=config, application=application, user=user)
        return response

    def push_webhook_to_sqs(self, payload, priority=1, application="", user=""):
        try:
            print("Push.py.push_webhook_to_sqs ")
            queue_name = ([k for k, v in self.core_settings["webhook_sqs_list"].items() if int(priority) in range(
                int(v.split("-")[0]), int(v.split("-")[1])+1)])[0] or list(self.core_settings["webhook_sqs_list"].keys())[0]
            QueueUrl = self.core_settings[self.app_env]["sqs_url"] + queue_name
            print("****************", QueueUrl)
            sqs_client = boto3.Session(profile_name=BOTO_ENV_DICTIONARY[self.app_env]["profile_name"]).client(
                'sqs') if self.app_env in ["local", "local-dev"] else boto3.client('sqs', BOTO_ENV_DICTIONARY[self.app_env]["region"])
            payload['uuid'] = self.generate_model_uuid4(application)
            payload = {
                'type': 'webhook',
                'priority': priority,
                'user_id': user,
                'application': application,
                'data': payload
            }

            response = sqs_client.send_message(
                QueueUrl=QueueUrl,
                MessageBody=json.dumps(payload), MessageGroupId=application)
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                final_response = {'status': True, 'response': response}
            else:
                final_response = {'status': False}
        except ClientError as e:
            print(str(e))
            final_response = {'status': False}
        return final_response

    def generate_model_uuid4(self, prefix=""):
        _uuid = str(uuid.uuid4()).replace("-", "")
        _prefix = '{}'.format(prefix)
        return "{}{}".format(_prefix, _uuid[len(_prefix):][:32]).lower()

    def validate_scheduler_payload(self, scheduler):
        attempts = scheduler.get("attempts", 0) if scheduler.get(
            "attempts", 0) < 10 else 0
        required_fields = {"interval_time": scheduler.get("interval_time", ""),
                           "attempts": attempts
                           }
        if not all(required_fields.values()):
            raise Exception({"request_status": "failure", "error_meta": [
                            'Validation Failed for Scheduler.']})
