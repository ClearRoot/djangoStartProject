from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from projectApp.forms import ProjectCreationForm
from projectApp.models import Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    success_url = reverse_lazy('articleApp:list')
    template_name = 'projectApp/create.html'
