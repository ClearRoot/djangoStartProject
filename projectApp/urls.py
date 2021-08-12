from django.urls import path

from projectApp.views import ProjectCreateView

app_name = 'projectApp'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
]
