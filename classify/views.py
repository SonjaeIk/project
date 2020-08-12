from django.shortcuts import  get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Review_Classfiy, Review_data 
from django.views import generic
from .forms import ReviewClassifyForm
import datetime
from django import forms


# Create your views here.


# def css_test(request):
#     # data = Review_data.objects.all()
#     return render(request, 'classify/css_test.html')

# def css_test2(request):
#     # data = Review_data.objects.all()
#     return render(request, 'classify/css_testing.html')

def main(request):
    data = Review_data.objects.all()
    return render(request, 'classify/main.html')

def annotate(request, review_data_id = 1):
    now = datetime.datetime.now()
    data = Review_data.objects.filter(id = review_data_id)
    # reivew_id = Review_data.objects.values('id')
    category = ['c1', 'c2', 'c3', 'c4']
    if request.method == 'POST':
        choice = request.POST.getlist('choice')
        form = ReviewClassifyForm()
        classify = form.save(commit = False)
        classify.user = request.user
        classify.review_id = Review_data.objects.get(id = review_data_id)
        classify.classify = choice
        classify.relase_date = now
        classify.save()
        number = review_data_id + 1 
        if number >= 1500:
            return redirect('/')
        # text = 'classify/{}'.format(str(number))     
        return redirect('/{}'.format(str(number)))#("FINISH") #, pk = review_data_id)
    else:
        print('ERROR')
    return render(request, 'classify/classify.html', {'datas': data,
                                                     'categorys' : category}) ## 데이터 셋 하나만 보여주기 

# def detail(request, review_data_id):
#     data = Review_data.objects.filter(pk=review_data_id)
#     gory = ['중식', '한식', '양식', '일식']
#     # reivew_id = Review_data.objects.values('id')
#     return render(request, 'classify/testing1.html', {'datas': data,
#                                                       'gorys' : gory}) ## 데이터 셋 하나만 보여주기 


# def show_first_data(request, review_data_id = 1):
#     now = datetime.datetime.now()
#     data = Review_data.objects.filter(id = review_data_id)
#     # reivew_id = Review_data.objects.values('id')
#     category = ['c1', 'c2', 'c3', 'c4']
#     if request.method == 'POST':
#         choice = request.POST.get('choice' '')
#         form = ReviewClassifyForm()
#         classify = form.save(commit = False)
#         classify.user = request.user
#         classify.review_id = Review_data.objects.get(id = review_data_id)
#         classify.classify = choice
#         classify.relase_date = now
#         classify.save()
#         number = review_data_id + 1 
#         if number >= 1500:
#             return redirect('classify/index.html')
#         text = 'classify/{}'.format(str(number))     
#         return redirect(text)#("FINISH") #, pk = review_data_id)
#     else:
#         print('ERROR')
#     return render(request, 'classify/testing.html', {'datas': data,
#                                                      'categorys' : category}) ## 데이터 셋 하나만 보여주기 


# def test(request, review_data_id):
#     data = Review_data.objects.filter(pk=review_data_id)
#     # reivew_id = Review_data.objects.values('id')
#     category = ['c1', 'c2', 'c3', 'c4']
#     if request.method == 'POST':
#         form = ReviewClassifyForm(request.POST)
#         a = request.POST.getlist('choice')
#         if form.is_valid():
#             form = form.cleaned_data
#             classify = form['choice']
#             classfication = form.save(commit = False)
#             classfication.user = request.user
#             classfication.reivew_id = review_data_id
#             classfication.classify = a
#             classfication.release_date = now
#             classfication.save()
#             return redirect('classify:main') #, pk = review_data_id)
#     return render(request, 'classify/testing.html', {'datas': data,
#                                                      'categorys' : category}) ## 데이터 셋 하나만 보여주기 
    

# def main_page(request):
#     if request.method == 'POST':
#         form = ReviewClassifyForm(request.POST)
#         if form.is_valid():
#             # Review_Classfiy.release_date = now
#             form.save()
#             return redirect('classify/index.html')
#     else:
#         form = ReviewClassifyForm()
#     return render(request, 'classify/index.html', {'form':form})