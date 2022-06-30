from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render

def search(request):          
    title =  request.GET.get('search')
    status = Blog.objects.filter(title__icontains=title)
    return render(request,'search.html',{'status':status})


def index(request):
    blog=Blog.objects.all()
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:            
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    return render(request,'index.html',{'blog':blog, 'posts':posts})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    if request.method=='POST':
        blog=Blog()
        blog.title=request.POST['title']
        blog.body=request.POST['body']
        blog.date=timezone.datetime.now()
        blog.save()
        return redirect('/')

    else:
        return render(request,'new.html')

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method=='POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()

        return redirect('/' + str(blog.id))
    else:
        return render(request, 'edit.html', {'blog':blog})

def delete(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    blog.delete()

    return redirect('/')