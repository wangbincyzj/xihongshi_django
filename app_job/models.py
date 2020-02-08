from app_user.models import BaseModel
from django.db import models


class Job(BaseModel):
    name = models.CharField(max_length=32)  # 标题
    salary = models.CharField(max_length=32)  # 薪水
    company_name = models.CharField(max_length=32)  # 公司名
    experience = models.CharField(max_length=32)  # 经验要求
    education = models.CharField(max_length=32)  # 学历要求
    address = models.CharField(max_length=128)  # 地址
    responsibilities = models.TextField()  # 岗位职责
    requirements = models.TextField()  # 入职要求
    features = models.CharField(max_length=128)  # 公司福利
    desc = models.CharField(max_length=128)  # 备注
    top = models.IntegerField(default=0)  # 顺序
    pub_user = models.CharField(max_length=32, null=True)  # 发布人账户
    # id_delete字段确定是否下架
