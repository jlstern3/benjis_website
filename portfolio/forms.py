
# from django.forms import ModelForm
from django import forms
from .models import Article, User, Plant, Recipe, Note
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

# class ArticleForm(ModelForm):
class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields="__all__"
        # can use exclude = ['name of field'] as well 

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"

class PlantForm(forms.ModelForm):
    class Meta:
        model=Plant
        fields="__all__"

class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields="__all__"

class NoteForm(forms.ModelForm):
    class Meta:
        model=Note
        # fields="__all__"
        exclude=['written_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper
        self.helper.form_method = 'post'

