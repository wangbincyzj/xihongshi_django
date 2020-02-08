from django.http import JsonResponse, HttpResponse
from django.views import View
import requests
import json


# /spider/chinanews/(?P<path.+>)  中国新闻网爬虫接口
def china_news(request, *args, **kwargs):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36",
        "Referer": "https://m.chinanews.com/wap/home",
        "Host": "m.chinanews.com",
    }
    real_path = request.get_full_path().split("/spider/")[-1]
    base_url = "https://m.chinanews.com/"
    real_url = base_url + real_path
    resp = requests.get(real_url, headers=headers)
    return JsonResponse(resp.json())


# /spider/xiaomi_mall/(?P<path.+>)
class MIMallView(View):
    headers = {
        "Origin": "https://m.mi.com",
        "Referer": "https://m.mi.com/",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "X-Requested-With": "XMLHttpRequest"
    }

    def post(self, request, *args, **kwargs):
        url = "https://m.mi.com/v1/" + kwargs.get("path")
        data = json.loads(request.body.decode())
        value = requests.post(url, data=data, headers=self.headers)
        response = HttpResponse(value, content_type="application/json; charset=utf-8")
        return response

    def get(self, request, *args, **kwargs):
        url = "https://m.mi.com" + kwargs.get("path")
        value = request.get(url, params=dict(request.GET), headers=self.headers)
        response = HttpResponse(value, content_type="application/json; charset=utf-8")
        return response

# /spider/maoyan/(?P<path.+>)
# http://m.maoyan.com/ajax/movieOnInfoList
class MovieView(View):
    headers = {
        "Referer": "http://m.maoyan.com/",
        "Host": "m.maoyan.com",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "X-Requested-With": "XMLHttpRequest"
    }
    def get(self, request, *args, **kwargs):
        url = "http://m.maoyan.com/" + kwargs.get("path")
        resp = requests.get(url, headers=self.headers)
        return JsonResponse(resp.json())

























