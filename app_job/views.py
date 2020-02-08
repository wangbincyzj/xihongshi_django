from django.http import JsonResponse
from app_job.models import Job
from django.core.paginator import Paginator
from app_user.views import Utils
from django.views import View


# /api/job/(?P<id>\d*)
class JobView(View):
    rules = [
        ["name", 1, 20], ["salary", 1, 20], ["company_name", 1, 32],
        ["experience", 1, 10], ["education", 1, 10], ["address", 1, 100],
        "responsibilities", "requirements", ["features", 1, 100], "desc"
    ]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        if id:
            pass
        else:
            page = request.GET.get("page", 1)
            size = request.GET.get("size", 10)
            models = Job.objects.all().order_by("-id")
            pager = Paginator(models, size)
            return_models = pager.get_page(page).object_list.values()
            return Utils.response(200, "success", data=list(return_models), num_pages=pager.num_pages,
                                  total=pager.count)

    @Utils.token_check
    def post(self, request, *args, **kwargs):
        check = Utils.length_check(request.JSON, rules=JobView.rules)
        if not check:
            return Utils.response(404, "数据格式非法")
        else:
            Job.objects.create(pub_user=request.user.username, **request.JSON)
            return Utils.response(200, "success")

    @Utils.token_check
    @Utils.admin_check
    def put(self, request, *args, **kwargs):
        pass

    @Utils.token_check
    @Utils.admin_check
    def delete(self, request, *args, **kwargs):
        id = request.JSON.get("id")
        Job.objects.filter(id=id).update(is_delete=True)
        return Utils.response(200, "success")
