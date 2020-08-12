# -*- coding: utf-8 -*-

from django import forms 
from .models import Review_Classfiy

class ReviewClassifyForm(forms.ModelForm):
    class Meta:
        model = Review_Classfiy
        fields = ['classify']
 