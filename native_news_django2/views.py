from django.http import JsonResponse
from django.conf import settings
from fdfs_client.client import Fdfs_client

CLIENT = Fdfs_client(conf_path=settings.FDFS_CLIENT_CONF)
SERVER_URL = settings.FDFS_SERVER_URL


# /upload/ [POST]
def upload(request):
    if request.method == "POST":
        print(request.body)
        file = request.FILES.get("file")
        resp = CLIENT.upload_appender_by_buffer(file.read())
        filename = resp.get("Remote file_id").replace("\\", "/")
        filepath = SERVER_URL + filename
        print(filepath)
        return JsonResponse({"code": 200, "msg": "上传成功",
                             "data": {"filename": filename, "filepath": filepath}})
