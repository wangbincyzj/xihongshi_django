from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class CORSMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response.status_code = 200
        if response.status_code == 403:
            response.status_code = 200
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Methods'] = "*"
        response['Access-Control-Max-Age'] = "1000"
        response['Access-Control-Allow-Headers'] = "*"
        if request.method == "OPTIONS" or request.method == "POST":
            if not response:
                response = HttpResponse("ok")
            if request.method == "OPTIONS":
                response = HttpResponse("ok")
            response['Access-Control-Allow-Origin'] = "*"
            response['Access-Control-Allow-Methods'] = "GET, HEAD, POST"
            response['Access-Control-Max-Age'] = "1000"
            response['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept,token,Access-Token"
            return response
        return response
