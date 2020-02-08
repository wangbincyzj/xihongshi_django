from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views import View
from app_nativeNews.models import Publisher
from app_nativeNews.models import News
from app_user.views import Utils


# /api/native_news/media/
class MediaView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        if id:
            model = Publisher.objects.filter(id=id).first()
            return Utils.response(200, "success", model_to_dict(model))
        else:
            size = request.GET.get("size", 10)
            page = request.GET.get("page", 1)
            models = Publisher.objects.all().order_by("-id")
            if page == "0":
                return Utils.response(200, "success", data=list(models.values()))
            pager = Paginator(models, size)
            return_models = pager.get_page(page).object_list.values()
            return Utils.response(200, "success", data=list(return_models), num_pages=pager.num_pages,
                                  total=pager.count)

    @Utils.token_check
    def post(self, request, *args, **kwargs):
        name = request.JSON.get("name")
        address = request.JSON.get("address")
        desc = request.JSON.get("desc")
        charge_person_name = request.JSON.get("charge_person_name")
        charge_person_phone = request.JSON.get("charge_person_phone")
        logo = request.JSON.get("logo")

        if not all([name, address, desc, charge_person_name, charge_person_phone]):
            return Utils.response(404, "数据不完整")
        same_model = Publisher.objects.filter(name=name)
        if same_model:
            return Utils.response(404, "存在相同名称")
        Publisher.objects.create(
            name=name, address=address, desc=desc,
            charge_person_phone=charge_person_phone,
            charge_person_name=charge_person_name,
            logo=logo
        )
        return Utils.response(200, "ok")

    @Utils.token_check
    @Utils.admin_check
    def put(self, request, *args, **kwargs):
        name = request.JSON.get("data").get("name")
        same_model = Publisher.objects.filter(name=name)
        if len(same_model) > 1:
            return Utils.response(404, "存在相同名称")
        Publisher.objects.filter(id=request.JSON.get("id")).update(**request.JSON.get("data"))
        model = Publisher.objects.filter(id=request.JSON.get("id")).first()
        return Utils.response(200, "success", data=model_to_dict(model))

    @Utils.token_check
    @Utils.admin_check
    def delete(self, request, *args, **kwargs):
        print(request.body)
        model = Publisher.objects.filter(id=request.JSON.get("id"))
        if not model:
            return Utils.response(404, "无数据")
        data = model_to_dict(model.first())
        model.delete()
        return Utils.response(200, "success", data=data)


# /api/native_news/news/
class NativeNewsView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        if id:
            model = News.objects.filter(id=id).first()
            return Utils.response(200, "success", model_to_dict(model))
        else:  # todo 代码冗余
            if request.GET.get("username"):  # getByUsername
                username = request.GET.get("username")
                models = News.objects.filter(pub_user=username)
                return Utils.response(200, "success", data=list(models.values()))
            else:
                size = request.GET.get("size", 10)
                page = request.GET.get("page", 1)
                models = News.objects.all().order_by("-id")
                pager = Paginator(models, size)
                return_models = pager.get_page(page).object_list.values()
                return Utils.response(200, "success", data=list(return_models), num_pages=pager.num_pages,
                                      total=pager.count)

    @Utils.token_check
    def post(self, request, *args, **kwargs):
        title = request.JSON.get("title")
        pubtime = request.JSON.get("pubtime")
        pub_user = request.user.username
        picture = request.JSON.get("picture")
        content = request.JSON.get("content")
        features = request.JSON.get("features")  # 可以没有
        source = request.JSON.get("source")
        md_content = request.JSON.get("md_content")
        if not all([title, pubtime, picture, content, source]):
            return Utils.response(404, "数据不完整")
        News.objects.create(title=title,
                            pubtime=pubtime,
                            picture=picture,
                            content=content,
                            features=features,
                            md_content=md_content,
                            pub_user=pub_user,
                            source=source)
        return Utils.response(200, "ok")

    def delete(self, request, *args, **kwargs):
        id = request.JSON.get("id")
        News.objects.filter(id=id).delete()
        return Utils.response(200, "success")

    def put(self, request, *args, **kwargs):
        News.objects.filter(id=request.JSON.get("id")).update(**request.JSON.get("data"))
        model = News.objects.filter(id=request.JSON.get("id")).first()
        return Utils.response(200, "success", data=model_to_dict(model))
