from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from info.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'info/content.html', context=context)

def one_post(request, post_id):
    return render(request, 'info/detail_post.html', context={'post':Post.objects.get(pk=post_id)})

@login_required
def add_like(request, post_id):
    post = Post.objects.get(pk=post_id)
    #print(post.likes.all())
    if request.user in post.likes.all():
        print('delete')
        post.likes.remove(request.user)
    else:
        print('append like')
        post.likes.add(request.user)
    return redirect(f'/post/{post_id}')

def about(request):
    return HttpResponse("<h2>About</h2>")

@login_required
def add_post(request):
    form = AddPostForm()
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('/')
    data = {
        'form': form
    }
    return render(request, 'info/add_post.html', context=data)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(request, username=name, password=p)
            if user:
                login(request, user)
                messages.success(request, f'Hi {name.title()}, welcome back!')
                return redirect('home')
    data = {'form': form}
    return render(request, 'info/login.html', context=data)
@login_required
def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['username']
            pas = form.cleaned_data['password1']
            user = authenticate(request, username=name, password=pas)
            login(request, user)
            return redirect('/')
    data = {'form': form}
    return render(request, 'info/register.html', context=data)
@login_required
def profile(request, user_id):
    p = get_object_or_404(User, pk=user_id)
    data = {'profile': p}
    return render(request, 'info/profile.html', context=data)



