from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleApp.models import Article
from likeApp.models import LikeRecord


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])

        like_record = LikeRecord.objects.filter(user=user, article=article)

        if like_record.exists():
            return HttpResponseRedirect(reverse('articleApp:detail', kwargs={'pk': kwargs['article_pk']}))
        else:
            LikeRecord(user=user, article=article).save()

        article.like += 1
        article.save()

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleApp:detail', kwargs={'pk': kwargs['article_pk']})
