from django.utils.deprecation import MiddlewareMixin
import json


class JsonParseMiddleware(MiddlewareMixin):

    def process_request(self, request):
        try:
            request.JSON = json.loads(request.body.decode("utf-8"))
        except Exception as e:
            request.JSON = {}