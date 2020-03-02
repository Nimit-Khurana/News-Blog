from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('json_news', views.display, name='display'),
]