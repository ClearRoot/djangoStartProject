from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.models import HelloWorld


# Create your views here.
def hello_page(request):
    if request.method == 'POST':
        temp = request.POST.get('input_text')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accounts:hello'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accounts/hello_world.html',
                      context={'hello_world_list': hello_world_list})
