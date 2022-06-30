from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import re

class Post(models.Model):   
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    name = models.CharField(max_length=20, null=True)
    # 1. 좋아요를 위한 다대다 필드 추가 ( 한 줄이면 충분! 구글링 하면 나옵니다! )
    # 작성하고 makemigrations와 migrate 해주기
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='like_user_set',through='Like')

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]
    
    def like_count(self):
        return self.like_user_set.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    contents = models.TextField()

    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.contents

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)