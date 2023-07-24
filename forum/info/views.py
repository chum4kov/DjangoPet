from django.http import HttpResponse
from django.shortcuts import render
from info.models import *
# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'info/content.html', context=context)

def one_post(request, post_id):
    return render(request, 'info/detail_post.html', context={'post':Post.objects.get(pk=post_id)})


def add_like(request, post_id):
    return redirect