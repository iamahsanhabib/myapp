from django.shortcuts import render, redirect

from django.http import HttpResponse


def index(request):
    return render(request,'home/index.html')
    #return HttpResponse("Hello, world. You're at the polls index.")
