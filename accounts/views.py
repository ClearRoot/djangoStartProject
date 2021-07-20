from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.forms import AccountCreationForm
from accounts.models import HelloWorld


# Create your views here.
def hello_page(request):
    if request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect(reverse('accounts:login'))


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:hello')
    template_name = 'accounts/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accounts/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accounts:hello')
    template_name = 'accounts/update.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return  super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return  super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accounts:hello')
    template_name = 'accounts/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))
