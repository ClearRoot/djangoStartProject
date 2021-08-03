from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from articleApp.forms import ArticleCreationForm
from articleApp.models import Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('articleApp:list')
    template_name = 'articleApp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)
