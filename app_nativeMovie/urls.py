from django.urls import path, re_path
from app_nativeMovie import views


# /api/movie/
urlpatterns = [
    path(r"", views.MovieView.as_view()),
]