from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
def home(request):
    return render(request, 'login_app/index.html')
"""
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'login_app/login.html', context={})

def register_user(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'login_app/register.html', context={'form':form})"""

class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'login_app/register.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'login_app/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')

