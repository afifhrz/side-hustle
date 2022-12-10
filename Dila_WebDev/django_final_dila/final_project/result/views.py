from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from calculation.models import trx_calculation
from result.models import trx_result
from django.contrib.auth.models import User

# Create your views here.
def index(request,id=0):
    data_user = User.objects.order_by('-last_login').first()
    if id==0:
        data_trx_calc = trx_calculation.objects.filter(user_id=data_user).last()
    else:
        data_trx_calc = trx_calculation.objects.filter(id=id)[0]
    
    data_trx_result_bs = trx_result.objects.filter(trx_calculation_id = data_trx_calc, type_calculation="Black Scholes")
    data_trx_result_mc = trx_result.objects.filter(trx_calculation_id = data_trx_calc, type_calculation="Monte Carlo")
    context = {
        'title' : 'Soca',
        'active_page':'result',
        'trx_calc':data_trx_calc,
        'trx_result_bs':data_trx_result_bs,
        'trx_result_mc':data_trx_result_mc,
    }
    return render(request, 'result/index.html', context)