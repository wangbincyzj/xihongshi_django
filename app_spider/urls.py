from django.urls import path, re_path
from app_spider.views import china_news, MIMallView, MovieView
# /spider/
urlpatterns = [
    re_path("^chinanews/(?P<path>.+)$", china_news),
    re_path("^xiaomi_mall/(?P<path>.+)$", MIMallView.as_view()),
    re_path("^maoyan/(?P<path>.+)$", MovieView.as_view()),  # /spider/maoyan/(?P<path.+>)
]