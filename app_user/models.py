from django.db import models
from utils.models import BaseModel


class UserInfo(BaseModel):
    nickname = models.CharField(max_length=16, default="未命名管理员")  # 昵称
    username = models.CharField(max_length=16, unique=True)  # 用户名
    password = models.CharField(max_length=64)  # 用户密码
    email = models.CharField(max_length=64, null=True)  # 邮箱
    avatar = models.CharField(max_length=128, default="https://cn.vuejs.org/images/logo.png")
    token = models.CharField(max_length=64)
    user_role = models.ForeignKey(to="Role", null=True, on_delete=models.SET_NULL)  # 用户角色


class Role(BaseModel):
    role_name = models.CharField(max_length=16, unique=True)  # 角色名
    role_desc = models.CharField(max_length=128)  # 角色描述

# class Permission(BaseModel):
#     permission_name = models.CharField(max_length=16)  # 权限名
#     permission_desc = models.CharField(max_length=128)  # 权限描述
#     api_path = models.CharField(max_length=128)  # api路径
#     api_level = models.IntegerField()  # api等级 0 不可读,不可写  1 可读,不可写   2 可读可写
