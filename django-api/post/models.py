from tkinter import CASCADE
from django.db import models
from common.models import BaseModel, SoftDeleteModel
from user.models import User

# Create your models here.

class Post(BaseModel, SoftDeleteModel):
    body = models.TextField(null=False)
    user = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE,
    )
    #categories = models.ManyToManyField(Category, through='CategoryPost')