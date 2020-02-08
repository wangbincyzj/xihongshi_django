from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse


class ErrorMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        return JsonResponse({"code": 500, "msg": "服务器内部错误", "exc": str(exception)})
