from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
class Diary(models.Model):
    title=models.CharField(max_length=50,default='제목 없음')
    body=models.TextField(null=False)
    date=models.DateTimeField('date published')
    mood=models.CharField(max_length=10,default='보통')
    image=models.ImageField(upload_to='images/',default='null')
    image_thumbnail=ImageSpecField(source='image',processors=[ResizeToFill(80,100)])
    kakao=models.CharField(max_length=50,default='kakao')
    def sum(self):
        return self.body[:5]