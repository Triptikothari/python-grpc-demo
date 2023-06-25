from .base import *
bypass_authentication = False

try:
    from .local_parameter_store import *
    bypass_authentication = True
except ImportError:
    try:
        from .aws_parameter_store import *
    except ImportError as e:
        e.args = tuple(
            ['%s (Not able to connect AWS parameter store)' % e.args[0]])
        raise e
# code for authorisation
# from routing.urls import grpc_handlers


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": [
            redis_parameter_store['DEFAULT']['LOCATION']
        ],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            "SOCKET_TIMEOUT": 5,  # in seconds
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        }
    },
}

DATABASES = {
    'default': {
        'ENGINE': database_parameter_store['DEFAULT']['ENGINE'],
        'NAME': database_parameter_store['DEFAULT']['NAME'],
        'USER': database_parameter_store['DEFAULT']['USER'],
        'PASSWORD': database_parameter_store['DEFAULT']['PASSWORD'],
        'HOST': database_parameter_store['DEFAULT']['HOST'],
        'PORT': database_parameter_store['DEFAULT']['PORT'],
    },
    'secondary' :{
        'ENGINE': database_parameter_store['SECONDARY']['ENGINE'],
        'NAME': database_parameter_store['SECONDARY']['NAME'],
        'USER': database_parameter_store['SECONDARY']['USER'],
        'PASSWORD': database_parameter_store['SECONDARY']['PASSWORD'],
        'HOST': database_parameter_store['SECONDARY']['HOST'],
        'PORT': database_parameter_store['SECONDARY']['PORT'],
    }
}


# CORS [START]
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'cache',
    'cookie',
    'hash',
    'key'
)
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
# CORS [END]

ALLOWED_HOSTS = ['*']


DEBUG = True

APP_ENV = miscellaneous_parameter_value['ENV']
