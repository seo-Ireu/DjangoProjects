from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True,related_name='comments')
    contents=models.CharField(max_length=200)

    def __str__(self):
        return self.contents