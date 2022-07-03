from django.shortcuts import render, redirect, get_object_or_404
from .forms import PicturePost
from .models import Picture

def home(request):
    posts = Picture.objects.all()
    return render(request, 'home.html', {'posts': posts})

def new(request):
    # 1. 입력된 내용 처리 : POST
    if request.method == 'POST':
        form = PicturePost(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('/')
            
    # 2. 빈 페이지 띄워주는 기능 : GET
    else:
        form = PicturePost()
        return render(request, 'new.html', {'form': form})

def detail(request, post_id):
    post = get_object_or_404(Picture, pk=post_id)
    return render(request, 'detail.html', {'post' : post})

def delete(request, post_id):
    post = Picture.objects.get(pk = post_id)
    post.delete()
    return redirect('/') 