from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello_page(request):
    return render(request, 'accounts/hello_world.html')
