from django.urls import path, re_path, include
from native_news_django2.views import upload

urlpatterns = [
    path("upload/", upload),  # 上传图片api直接返回地址
    path("spider/", include("app_spider.urls")),  # 爬虫数据转发


    path("api/user/", include("app_user.urls")),  # 用户相关
    path("api/job/", include("app_job.urls")),  # 本地工作岗位
    path("api/native_news/", include("app_nativeNews.urls")),  # 本地新闻相关
    path("api/mall/", include("app_mall.urls")),  # 商城
    path("api/movie/", include("app_nativeMovie.urls"))  # 商城

]
