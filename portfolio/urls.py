from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('create_user', views.create_user),
    path('logout', views.logout),
    path('home', views.home),
    path('blog/new', views.new_blog_post),
    path('grow', views.grow),
    path('grow/plant_details', views.plant_details),
    path('grow/houseplant_details', views.houseplant_details),
    path('grow/veg', views.fruit_veg),
    path('grow/houseplants', views.houseplants),
    path('grow/landscaping', views.landscaping),
    path('grow/herbs', views.herbs),
]