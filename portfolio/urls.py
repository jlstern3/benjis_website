from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('create_user', views.create_user),
    path('home', views.home),
    path('blog/new', views.new_blog_post),
    path('plant_details', views.plant_details),
    path('houseplant_details', views.houseplant_details),
    path('grow', views.grow),
    path('grow/veg', views.fruit_veg),
]