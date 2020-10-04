from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User

from .models import *

class PostForm(ModelForm):
    class Meta:
        model = WardrobePost
        fields = '__all__'
        exclude = ('date_created',)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')