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
    path('note/new', views.new_note),
    path('note/create', views.create_note),
    path('note/<int:note_id>/edit', views.edit_note),
    path('note/<int:note_id>/update', views.update_note),
    path('recipe/new', views.new_recipe),
    path('plant/new', views.new_plant),
    path('plant/create', views.create_plant),
    path('plant/delete/<int:plant_id>', views.delete_plant),
    path('plant/<int:plant_id>/update', views.update_plant),
    path('plant/<int:plant_id>/edit', views.edit_plant),
    path('plant/<int:plant_id>/like', views.like_plant),
    path('plant_search', views.plant_search),
    path('plant/<int:plant_id>/unlike_plant', views.unlike_plant),
    path('grow', views.grow),
    path('grow/all_plants', views.all_plants),
    path('grow/details/<int:plant_id>', views.plant_details),
    path('grow/houseplant_details', views.houseplant_details),
    path('grow/veg', views.fruit_veg),
    path('grow/houseplants', views.houseplants),
    path('grow/landscaping', views.landscaping),
    path('grow/herbs', views.herbs),
]