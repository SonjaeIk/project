from django.contrib import admin
from annotate.models import Question, Choice
# Register your models here.
#### admin  사이트에 model 등록

admin.site.register(Question)
admin.site.register(Choice)
