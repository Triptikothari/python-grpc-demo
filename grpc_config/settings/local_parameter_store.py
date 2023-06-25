miscellaneous_parameter_value = {
    "DEBUG": True,
    "ENV": 'local',
}
database_parameter_store = {
    'DEFAULT': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "userproto",
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
    'SECONDARY': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "userproto",
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
}
redis_parameter_store = {
    "DEFAULT": {
        "LOCATION": "redis://127.0.0.1:6379/1"
    },
}
region_parameter_store = {
    "default": "us-east-1"
}
