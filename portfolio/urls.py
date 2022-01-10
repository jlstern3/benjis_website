from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('blog/new', views.new_blog_post),
    path('plant_details', views.plant_details),
]