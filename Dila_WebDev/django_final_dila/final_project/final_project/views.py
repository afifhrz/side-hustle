from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

@csrf_protect
def index(request):
    if request.method == "POST":
        user = User.objects.create_user(request.POST['floatingText'], request.POST['floatingText'], request.POST['floatingPassword'])
    context = {
        'title' : 'Soca'
    }
    return render(request, 'signin.html', context)

@csrf_protect
def login_process(request):
    user = authenticate(username=request.POST['floatingInput'], password = request.POST['floatingPassword'])
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('home_page'))
    else:
        return HttpResponseRedirect(reverse('signin'))

def signup(request):
    context = {
        'title' : 'Soca'
    }
    return render(request, 'signup.html', context)