import uuid
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    # id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Project(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    

