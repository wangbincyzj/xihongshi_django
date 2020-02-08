from django.urls import path, re_path
from app_nativeNews import views
app_name = "app_spider"


# /api/native_news/
urlpatterns = [
    re_path(r"media/(?P<id>\d*)", views.MediaView.as_view()),
    re_path(r"news/(?P<id>\d*)", views.NativeNewsView.as_view()),
]