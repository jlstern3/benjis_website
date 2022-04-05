from django.contrib import admin
from .models import Note, Plant, Recipe, Article, User

# Register your models here.
admin.site.register(Note)
admin.site.register(Plant)
admin.site.register(Recipe)
admin.site.register(User)
admin.site.register(Article)