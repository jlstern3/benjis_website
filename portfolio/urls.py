from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('create_user', views.create_user),
    path('logout', views.logout),
    path('home', views.home),
    path('profile/<int:user_id>', views.profile),
    path('profile/<int:user_id>/edit', views.edit_profile),
    path('profile/<int:user_id>/update', views.update_profile),
    path('notes/new', views.new_note),
    path('grow', views.grow),
    path('grow/plant_details', views.plant_details),
    path('grow/houseplant_details', views.houseplant_details),
    path('grow/veg', views.fruit_veg),
    path('grow/houseplants', views.houseplants),
    path('grow/landscaping', views.landscaping),
    path('grow/herbs', views.herbs),
]