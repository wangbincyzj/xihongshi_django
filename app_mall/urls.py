from django.urls import path, re_path
from app_mall import views


# /api/mall/
urlpatterns = [
    path(r"", views.MallView.as_view()),
]