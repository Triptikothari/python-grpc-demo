from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from pg_config.settings import bypass_authentication
from config_routing.shared.utility.redis import RedisAccessor


class Authorization(object):

    def __init__(self, get_response):
        self.get_response = get_response
        self.authenticate_by = None
        self.authorized = False
        self.merchant_id = None

    def __call__(self, request):
        self.authenticate_by = None
        self.authorized = False
        self.merchant_id = None
        
        if self.request_is_exempted(request):
            response = self.get_response(request)
            return response

        self.set_authenticate_by(request)
        if self.authenticate_by == "cookie":
            self.authenticate_by_cookie(request)
        else:
            pass

        if bypass_authentication:
            self.authorized = True
            self.merchant_id = 4486
            self.merchant_allowed = True

        self.authenticate_by_database(request)

        if self.authorized:
            request.merchant_id = self.merchant_id
            response = self.get_response(request)
            return response
        response = Response(
            data={"status": False, "message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        response.render()
        return response

    def set_authenticate_by(self, request):
        if len(request.COOKIES) > 0 and request.COOKIES.get('easetoken'):
            self.authenticate_by = "cookie"
        else:
            self.authenticate_by = "cookie"
            # self.authenticate_by = "request_data"

    def authenticate_by_cookie(self, request):
        try:
            easetoken_value = request.COOKIES.get("easetoken", "")
            is_redis_key_present = RedisAccessor.checkKey(easetoken_value,connection='redis')
            if is_redis_key_present:
                redis_merchant_data = RedisAccessor.getData(easetoken_value,connection='redis')
                self.authorized = True
                self.merchant_id = redis_merchant_data.get("id")
            else:
                self.authorized = False

            
        except Exception as e:
            print("Excception in Auth - ",  str(e))
            pass

    def authenticate_by_database(self, request):
        try:
           
            self.merchant_allowed = 4486            
        except Exception as e:
            self.merchant_allowed = False                

    def request_is_exempted(self, request):
        return request.path_info in [
            "/api/v1/login",
            "/api/v1/report/report-callback"
        ]

    def process_view(self, request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called
        pass

    def process_exception(self, request, exception):
        # This code is executed if an exception is raised
        pass

    def process_template_response(self, request, response):
        # This code is executed if the response contains a render() method
        return response
