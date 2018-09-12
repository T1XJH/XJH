from django.shortcuts import render, redirect
from .models import MyblogInfo

# Create your views here.

def index(request):
    infolists = MyblogInfo.objects.all()

    return render(request, 'blogs/index.html', {"items": infolists})

def about(request):
    return render(request, 'blogs/about.html',)

def share(request):
    return render(request, 'blogs/share.html',)

def list(request):
    infolists = MyblogInfo.objects.all()
    pic = MyblogInfo.objects.filter("uploadimg")
    return render(request, 'blogs/list.html', {"items": infolists, "pic": pic})

def fengmian(request):
    return render(request, 'blogs/fengmian.html', )

def info(request):
    return render(request, 'blogs/info.html', )

def time(request):
    return render(request, 'blogs/time.html')


