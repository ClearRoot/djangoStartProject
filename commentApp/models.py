from django.contrib.auth.models import User
from django.db import models

from articleApp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)

    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)
