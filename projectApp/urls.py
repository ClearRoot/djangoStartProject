from django.urls import path

from projectApp.views import ProjectCreateView, ProjectDetailView, ProjectListView

app_name = 'projectApp'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),

    path('list/', ProjectListView.as_view(), name='list'),
]
