from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=50,default='제목 없음')
    body=models.TextField(null=False)
    date=models.DateTimeField('date published')

    def sum(self):
        return self.body[:15]
