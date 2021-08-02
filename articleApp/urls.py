from django.urls import path
from django.views.generic import TemplateView

app_name = 'articleApp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleApp/list.html'), name='list'),
]