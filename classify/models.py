from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Review_data(models.Model): ### 리뷰를 담을 곳
    id = models.AutoField(primary_key = True)
    nickname = models.CharField(max_length = 20)
    date = models.CharField(max_length = 30)
    rating = models.IntegerField()
    comment = models.TextField(null = True)

class Review_Classfiy(models.Model):
    id = models.AutoField(primary_key = True) ## 각각의 코멘트에 대한 ID 부여 
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True) ## User 정보 담는 곳
    review_id = models.ForeignKey(Review_data, on_delete = models.CASCADE)
    classify = models.CharField(max_length = 20, null = True)
    release_date = models.DateField(default = timezone.now)
    