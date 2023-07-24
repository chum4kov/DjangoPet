from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=500,null=True)
    image = models.ImageField(upload_to='images/')
    likes = models.ManyToManyField(User, blank=True)
    #dislikes = models.ManyToManyField(User, blank=True)
    category = models.ManyToManyField('Category')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
