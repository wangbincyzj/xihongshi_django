from django.db import models


class BaseModel(models.Model):
    """模型抽象基类:创建时间,更新时间,删除标记"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    choice = ((0, "未删除"), (1, "已删除"))
    is_delete = models.BooleanField(choices=choice, default=0, verbose_name="删除标识")

    # 抽象模型类声明
    class Meta:
        abstract = True
