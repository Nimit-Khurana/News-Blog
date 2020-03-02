from django.shortcuts import render
from django.http import HttpResponse
from .script import news
import json


# Create your views here.
def index(request):
    return render(request, 'news.html')

def display(request):
    data = news()
    return render(request, 'html.html', {"data":data})