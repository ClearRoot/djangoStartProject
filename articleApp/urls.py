from django.urls import path
from django.views.generic import TemplateView

from articleApp.views import ArticleCreateView, ArticleDetailView

app_name = 'articleApp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleApp/list.html'), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
]
