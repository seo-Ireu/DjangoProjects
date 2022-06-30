from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Diary
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import auth
def index(request):
    d=Diary.objects.all()
    diary_list = Diary.objects.all()
    paginator = Paginator(diary_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:            
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    return render(request,'index.html',{'d':d, 'posts':posts})

def new(request):
    if request.method=='POST':
        d=Diary()
        d.title=request.POST['title']
        d.body=request.POST['body']
        d.date=timezone.datetime.now()
        d.mood=request.POST['mood']
        d.image=request.FILES['image']
        d.save()
        return redirect('/')
    else:
        return render(request,'new.html')

def edit(request,diary_id):
    d=get_object_or_404(Diary,pk=diary_id)
    if request.method=='POST':
        d.title=request.POST['title']
        d.body=request.POST['body']
        d.mood=request.POST['mood']
        d.save()
        return redirect('/'+str(d.id))
    else:
         return render(request,'edit.html',{'d':d})


def delete(request,diary_id):
    d=get_object_or_404(Diary,pk=diary_id)
    d.delete()

    return redirect('/')

def detail(request, diary_id):
    d= get_object_or_404(Diary,pk=diary_id)
    return render(request, 'detail.html', {'d':d})    

def signup(request):
    if request.method == 'POST':
        if request.POST['username']=='' or request.POST['password']=='':
            return render(request,'signup.html',{'error':'이름 비번 필수 입력'})
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
            name = request.POST['username']
            pw = request.POST['password']
            user = auth.authenticate(request, username=name, password=pw)


            if user is not None: # user가 잘 찾아진 경우
                    auth.login(request, user) # 로그인
                    return redirect('/')

            else:
                    return render(request, 'login.html',{'error':'이름 비밀번호를 확인'}) # error 객체 전달

    else:
            return render(request, 'login.html') # GET 방식으로 요청