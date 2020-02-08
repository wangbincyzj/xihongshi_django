from django.urls import path, re_path
from app_job.views import JobView

# api/job/
urlpatterns = [
    re_path(r"^(?P<id>\d*)$", JobView.as_view())
]
