from django.http import JsonResponse
from django.views import View
from django.core.paginator import Paginator
from app_user.models import UserInfo
from app_nativeMovie.models import NativeMovie
from app_mall.models import Mall
from app_nativeNews.models import News
from app_job.models import Job
import hashlib
import time
import datetime


class Utils:
    @staticmethod  # 装饰器 [headers token验证]
    def token_check(view_func):
        def return_func(request, *args, **kwargs):
            if args:
                request = args[0]
            token = request.headers.get("token")
            # 请求头没有token
            if not token:
                return JsonResponse({"code": 403, "msg": "请先登录"})
            # token验证,成功则注入request.user
            user = UserInfo.objects.filter(token=token).first()
            if not user:
                return JsonResponse({"code": 403, "msg": "登录信息失效"})
            else:
                request.user = user
                return view_func(request, *args, **kwargs)

        return return_func

    @staticmethod  # 装饰器 [super管理员 token验证]
    def admin_check(view_func):
        def return_func(request, *args, **kwargs):
            if args:
                request = args[0]
            if request.user.user_role_id != 1:
                return JsonResponse({"code": 403, "msg": "没有权限"})
            else:
                return view_func(request, *args, **kwargs)

        return return_func

    @staticmethod  # 通过用户名密码创建一个token
    def create_token(username, password):
        md5 = hashlib.md5()
        token_string = username + password + str(time.time())[:-7]
        md5.update(token_string.encode())
        return md5.hexdigest()

    @staticmethod  # 快速JSON返回
    def response(code, msg, data=None, **kwargs):
        return JsonResponse({"code": code, "msg": msg, "data": data, **kwargs})

    @staticmethod  # models字段长度验证
    # rules = [
    #     ["name"], ["desc2", 3, 10], "age", ["age2", 1,2]
    # ]
    def length_check(data: dict, rules: list):
        for i in rules:
            if isinstance(i, str):
                item = data.get(i)
                if not item:
                    return False
            else:
                item = data.get(i[0])
                if not item:
                    return False
                if len(i) == 3:
                    if len(item) < i[1] or len(item) > i[2]:
                        return False
        return True


# /api/user/login/  [POST]
def login(request, *args, **kwargs):
    if request.method == "POST":
        username = request.JSON.get("username")
        password = request.JSON.get("password")
        if len(username) < 4 or len(password) < 5:
            return Utils.response(400, "用户名或者密码格式错误")
        login_user = UserInfo.objects.filter(username=username).first()
        if login_user:
            if login_user.password == password:
                return JsonResponse({"code": 200,
                                     "msg": "登录成功",
                                     "data": {"token": login_user.token,
                                              "avatar": login_user.password,
                                              "create_time": login_user.create_time,
                                              }})
            else:
                return Utils.response(400, "存在相同用户名")
        user = UserInfo.objects.create(username=username, password=password)
        token = Utils.create_token(username, password)
        user.token = token
        user.user_role_id = 2
        user.save()
        return JsonResponse({"code": 200, "msg": "登录成功", "data": {"token": token,
                                                                  "avatar": user.avatar
                                                                  }})

    else:
        return Utils.response(500, "forbidden")


# /api/user/token_check/ [POST]
def token_check(request, *args, **kwargs):
    if request.method == "POST":
        token = request.JSON.get("token")
        model = UserInfo.objects.filter(token=token).first()
        if model:
            return Utils.response(200, "验证成功", user_type=model.user_role_id, username=model.username,
                                  avatar=model.avatar, create_time=model.create_time)
        else:
            return Utils.response(404, "token验证失败")


# /api/user/logout/  [POST]
@Utils.token_check
def logout(request, *args, **kwargs):
    print("logout")
    if request.method == "POST":
        print("post")
        request.user.token = Utils.create_token(request.user.username, request.user.password)
        request.user.save()
        return Utils.response(200, "注销成功")
    else:
        print("else")
        return Utils.response(500, "forbidden")


# /api/user/home_info/  [GET]
class HomeInfoView(View):
    def get_info(self, obj):
        user = UserInfo.objects.filter(create_time__day=obj["day"], create_time__month=obj["month"]).count()
        news = News.objects.filter(create_time__day=obj["day"], create_time__month=obj["month"]).count()
        order = Mall.objects.filter(create_time__day=obj["day"], create_time__month=obj["month"]).count()
        job = Job.objects.filter(create_time__day=obj["day"], create_time__month=obj["month"]).count()
        movie = NativeMovie.objects.filter(create_time__day=obj["day"], create_time__month=obj["month"]).count()
        obj["data"] = {"user": user, "news": news, "order": order, "job": job, "movie": movie}

    def get_total(self):
        user = UserInfo.objects.all().count()
        news = News.objects.all().count()
        order = Mall.objects.all().count()
        job = Job.objects.all().count()
        movie = NativeMovie.objects.all().count()
        return {"user": user, "news": news, "order": order, "job": job, "movie": movie}

    def get(self, request, *args, **kwargs):
        date_list = []  # 7天数据
        for i in range(0, 7):
            date_list.append({"month": (datetime.datetime.now() - datetime.timedelta(days=i)).month,
                              "day": (datetime.datetime.now() - datetime.timedelta(days=i)).day})
        for i in date_list:
            self.get_info(i)
        total_data = self.get_total()
        return Utils.response(200, "success", {"date_list": date_list, "total_data": total_data})

    def post(self, request):
        print(NativeMovie.objects.filter(create_time__month="02").count())
    # 首先获取今天日期然后得到一个星期的 日期列表
    # 构建一个函数传入日期,得到当天的注册用户,订单总数,新闻上传总数总数,招聘总数,电影总数


# /api/user/userinfo/ [POST]
class UserInfoView(View):
    @Utils.token_check
    def post(self, request, *args, **kwargs):
        request.user.avatar=request.JSON.get("avatar")
        request.user.save()
        return Utils.response(200, "success")

    def get(self, request):
        page = request.GET.get("page", 1)
        size = request.GET.get("size", 10)
        models = UserInfo.objects.all().order_by("-id").values()
        pager = Paginator(models, size)
        return_models = pager.get_page(page).object_list.values()
        return Utils.response(200, "success", data=list(return_models), num_pages=pager.num_pages,
                              total=pager.count)
