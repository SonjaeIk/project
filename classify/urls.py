# -*- coding: utf-8 -*-

from django.urls import path
from . import views


app_name = 'classify'

urlpatterns = [
    path('', views.main, name='main'),
    path('description/', views.description, name = 'description'), ## 단어들에 대한 Description
    path('<int:review_data_id>', views.annotate, name = 'annotate'),
]