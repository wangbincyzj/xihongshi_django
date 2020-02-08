from django.views import View
from app_user.views import Utils
from app_mall.models import Mall
from django.core.paginator import Paginator


# api/mall/
class MallView(View):
    @Utils.token_check
    def post(self, request, *args, **kwargs):
        username = request.JSON.get("username")
        data = request.JSON.get("data")
        data = str({"username": username, "data": data})
        Mall.objects.create(data=data)
        return Utils.response(200, "success")

    def get(self, request, *args, **kwargs):
        page = request.GET.get("page", 1)
        size = request.GET.get("size", 10)
        models = Mall.objects.all().order_by("-id")
        pager = Paginator(models, size)
        return_models = pager.get_page(page).object_list.values()
        return Utils.response(200, "success", data=list(return_models), num_pages=pager.num_pages,
                              total=pager.count)
