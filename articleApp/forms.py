from django.forms import ModelForm

from articleApp.models import Article


class ArticleCreationFirm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'content']
