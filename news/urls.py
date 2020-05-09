from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('json_news', views.display, name='display'),
    path('news', views.news_custom, name="news"),
    path('login_user', views.user_login, name='user_login'),
]