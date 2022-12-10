from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    data_user = User.objects.order_by('-last_login').first()
    context = {
        'title':'Soca',
        'active_page':'dashboard',
        'user':data_user
    }
    return render(request, 'dashboard/index.html', context)