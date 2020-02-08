from django.db import models
from utils.models import BaseModel


class News(BaseModel):
    title = models.CharField(max_length=32)  # 标题
    pubtime = models.DateTimeField()  # 发表时间
    pub_user = models.CharField(max_length=16, default="佚名")  # 从token中提取的提交人
    picture = models.FileField()  # 封面图
    content = models.TextField()  # 内容
    md_content = models.TextField(null=True)  # mark_down 初始内容
    features = models.CharField(max_length=64, null=True)  # 热点新闻, 独家新闻
    source = models.CharField(max_length=64)  # [新闻网,广播台...]
    desc = models.CharField(max_length=128, null=True)
    # publisher = models.ForeignKey(to="Publisher", on_delete=models.SET_NULL, null=True)


class Publisher(BaseModel):
    name = models.CharField(max_length=32)  # 媒体名称
    address = models.CharField(max_length=128)  # 媒体地址
    type = models.IntegerField(default=0)  # 类型 0:自媒体 1:机构
    desc = models.CharField(max_length=1024)  # 描述补充
    charge_person_name = models.CharField(max_length=16)  # 负责人姓名
    charge_person_phone = models.CharField(max_length=16)  # 负责人联系电话
    logo = models.CharField(max_length=128, default="https://cn.vuejs.org/images/logo.png")  # 品牌logo
