from django import forms


from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields="__all__"
        # can use exclude = ['name of field'] as well 