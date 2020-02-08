from django.urls import path, re_path
from app_user import views

# /api/user/
urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("userinfo/", views.UserInfoView.as_view()),
    path("token_check/", views.token_check),
    path("home_info/", views.HomeInfoView.as_view())
]



