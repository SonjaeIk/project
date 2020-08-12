# -*- coding: utf-8 -*-

from django.urls import path
from . import views


app_name = 'classify'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:review_data_id>', views.annotate, name = 'annotate'),
    # path('css_test_2/', views.css_test2, name = 'test2'),
    # path('classification/<int:review_data_id>', views.detail)
    # path('css_test/', views.css_test, name = 'test'),
    # path('test/', views.main_page, name='main_page'),
    # path('classify/1', views.test, name = 'fist_page'),
    # path('classify/<int:review_data_id>', views.detail, name = 'classfy_id'),   
]