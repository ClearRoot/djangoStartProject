from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from commentApp.forms import CommentCreationForm
from commentApp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentApp/create.html'

    def get_success_url(self):
        return reverse('articleApp:detail', kwargs={'pk': self.object.article.pk})
