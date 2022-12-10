from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    data_user = User.objects.order_by('-last_login').first()
    context = {
        'title' : 'Soca',
        'active_page':'help',
        'user':data_user
    }
    return render(request, 'help/index.html', context)