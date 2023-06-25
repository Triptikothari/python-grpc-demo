from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from routing.controllers.test import TestController

router = SimpleRouter()

api_routes = [
    path('v1/',include([
        path('test', TestController.as_view({'post': 'test'}), name="test")
    ])),
]


urlpatterns = api_routes
urlpatterns = format_suffix_patterns(urlpatterns)
