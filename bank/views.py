from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def single(request):
    return render(request,'singlepage.html')