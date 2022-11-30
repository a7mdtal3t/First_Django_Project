from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def index(request):
    url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=ad0b3bdb179c41e8a3bb9bdff0e26cd6'
    response = requests.get(url)
    jsonResponse = response.json()
    articles = jsonResponse['articles']
    return render(request, 'blog/index.html', {'articles': articles})
