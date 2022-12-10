from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from calculation.models import trx_calculation
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    data_user = User.objects.order_by('-last_login').first()
    data_result = trx_calculation.objects.filter(user_id=data_user)
    context = {
        'title' : 'Soca',
        'active_page':'history',
        'data_result':data_result,
        'user':data_user
    }
    return render(request, 'history/index.html', context)

# @csrf_protect
# def login(request):
#     return HttpResponseRedirect(reverse('home_page'))

# def signup(request):
#     context = {
#         'title' : 'Soca'
#     }
#     return render(request, 'signup.html', context)