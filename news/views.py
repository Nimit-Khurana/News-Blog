from django.shortcuts import render
from django.http import HttpResponse
from .script import news
from .models import User
from .extract import (
                extract,
                hindu_national,
                hindu_international,
                toi_national,
                toi_international,
                hindustan_feed_url
)
import json


# Create your views here.
def index(request):
    return render(request, 'news.html')

def display(request):
    data_api = news()
    return render(request, 'api_data.html',{"data":data_api})

def news_custom(request):
    option = request.GET['option']
    if option == "hindu_national":
        data = extract(hindu_national)
    elif option == "hindu_international":
        data = extract(hindu_international)
    elif option == "hindustan_times":
        data = extract(hindustan_feed_url)
    elif option == "toi_international":
        data = extract(toi_international)
    else:
        data = extract(toi_national)
    return render(request, "api_data.html", {"data": data})

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        User(username=username, password=password)
        print ("user created")
        return render(request, 'login.html')
    return render(request, 'login.html')