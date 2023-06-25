from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class CustomResponseMixin(ModelViewSet):

    def finalize_response(self, request, response, *args, **kwargs):
        """
        Returns the final response object.
        """
        if isinstance(response, Response):
            if not getattr(request, 'accepted_renderer', None):
                neg = self.perform_content_negotiation(request, force=True)
                request.accepted_renderer, request.accepted_media_type = neg

            response.accepted_renderer = request.accepted_renderer
            response.accepted_media_type = request.accepted_media_type
            response.renderer_context = self.get_renderer_context()

        if (response.status_code in [200]):
            response.status_code = 200
            response.data = {"success": True,
                             "data": response.data.get('data', [])}
        elif (response.status_code in [400]):
            response.status_code = 400
            response.data = {"success": False, "message": response.data.get(
                'message', 'Invalid Request')}
        elif (response.status_code in [401]):
            response.status_code = 401
            response.data = {"success": False, "message": response.data.get(
                'message', "You are not authorised to perform this action")}
        elif (response.status_code in [500]):
            response.status_code = 500
            response.data = {"success": False, "message": response.data.get(
                'message', "Something went wrong. Try again")}
        else:
            response.status_code = 403
            response.data = {"success": False,
                             "message": "Something went wrong. Try again"}
        return response
