from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.urls import reverse_lazy

from .forms import *
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
# Create your views here.
from .models import *

def home(request):
    tasks = Task.objects.filter(member=request.user.id)

    context = {
        'tasks': tasks
    }
    return render(request, 'todoapp/home.html', context=context)

def add(request):
    print(request.POST)
    text = request.POST['text-task']
    Task.objects.create(title=text, is_complete=False, member=request.user)
    return redirect('/')

def update(request, id_task):
    obj = Task.objects.get(id=id_task)
    obj.is_complete = not obj.is_complete
    obj.save()
    return redirect('/')

def delete(request, id_task):
    obj = Task.objects.get(id=id_task)
    obj.delete()
    return redirect('/')



class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'todoapp/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'todoapp/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('home')