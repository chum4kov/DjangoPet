from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)
    member = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True)
