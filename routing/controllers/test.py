from typing import Any
from rest_framework.response import Response
from routing.shared.utility.custom_mixins import CustomResponseMixin
from routing.services.test import TestService


class TestController(CustomResponseMixin):
    def __init__(self, **kwargs: Any) -> None:
        self.tests = TestService()
        super().__init__(**kwargs)

    def test(self, request):
        try:
            response = self.tests.fetch_data()
            print(response)
            if response['status'] != 200:
                return Response(response, response['status'])
            return Response(response, response['status'])
        except Exception as e:
            return Response({"message": str(e)}, 500)
