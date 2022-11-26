from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('This is my blog')


def hi(request):
    return HttpResponse('hiiiii')


def ahmed(request):
    return HttpResponse('Ahmeeeeeeeeeeeeeeeeeeeeeed')


def zeina(request):
    return HttpResponse('Zeeeeeeeiiiinaaaaaaaa')
