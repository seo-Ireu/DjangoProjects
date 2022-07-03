# Blog class를 기반으로 만들 것이기 때문에 blog 안에 form.py를 만들어준 것! models.py 여기 있자너
from django import forms
from .models import Picture

# 모델기반이 아니면 forms.Form
class PicturePost(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['title', 'content', 'image']