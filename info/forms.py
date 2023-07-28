from django import forms
from .models import *
from django.contrib.auth.forms import *
from captcha.fields import CaptchaField

class AddPostForm(forms.ModelForm):
    #post_name = forms.CharField(label='Название', max_length=100)
    #content = forms.CharField(label='Описание', max_length=500)
    class Meta:
        model = Post
        fields = ['name', 'content', 'image', 'category']
        widgets = {
            'name': forms.TextInput(),
            'content': forms.Textarea(attrs={'cols': 30})
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Имя')
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(), label='Повтор пароля')
    photo = forms.ImageField(upload_to='ava/', label='Фото')

    captcha = CaptchaField()

