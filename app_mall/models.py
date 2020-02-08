from django.db import models
from utils.models import BaseModel


class Mall(BaseModel):
    data = models.CharField(max_length=1024)



