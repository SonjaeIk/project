# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 00:01:17 2020

@author: Sonjaeik
"""


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")