from django.shortcuts import render


# Create your views here.
def hello_page(request):
    if request.method == 'POST':
        return render(request, 'accounts/hello_world.html',
                      context={'text': 'POST METHOD'})
    else:
        return render(request, 'accounts/hello_world.html',
                      context={'text': 'GET METHOD'})
