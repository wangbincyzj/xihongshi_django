from django.db import models
from utils.models import BaseModel


class NativeMovie(BaseModel):
    name = models.CharField(max_length=32)
    username = models.CharField(max_length=32, null=True)
    actors = models.CharField(max_length=128)
    picture = models.CharField(max_length=128)
    rate = models.CharField(max_length=16)
    scene = models.CharField(max_length=128)
