from django.shortcuts import render
from django.views import View
from app_user.views import Utils
from app_nativeMovie.models import NativeMovie
from django.core.paginator import Paginator


# api/movie/
class MovieView(View):
    rules = [
        "name", "actors", "picture", "scene"
    ]

    @Utils.token_check
    def post(self, request, *args, **kwargs):
        print(request.JSON)
        check = Utils.length_check(request.JSON, rules=MovieView.rules)
        if not check:
            return Utils.response(404, "数据格式非法")
        else:
            NativeMovie.objects.create(username=request.user.username, **request.JSON)
            return Utils.response(200, "success")

    def get(self, request, *args, **kwargs):
        page = request.GET.get("page", 1)
        size = request.GET.get("size", 10)
        models = NativeMovie.objects.all().order_by("-id")
        pager = Paginator(models, size)
        return_models = pager.get_page(page).object_list.values()
        return Utils.response(200, "success", data=list(return_models), num_pages=pager.num_pages,
                              total=pager.count)
