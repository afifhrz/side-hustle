from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_protect
from calculation.models import trx_calculation
from result.models import trx_result
from django.contrib.auth.models import User
from datetime import datetime

from scipy import stats
import random
import math
import pandas as pd
import numpy as np

# Create your views here.
def index(request):
    data_user = User.objects.order_by('-last_login').first()
    context = {
        'title':'Soca',
        'active_page':'calculation',
        'user':data_user
    }
    return render(request, 'calculation/index.html', context)

def black_scholes_cal(s_0, strike_price, partition_of_time, volatility, interest_rate, type):
    d1 = (math.log(s_0/strike_price) + (interest_rate + volatility**2/2) * partition_of_time) / (volatility * math.sqrt(partition_of_time))
    d2 = d1 - volatility * math.sqrt(partition_of_time)
    Nd1 = stats.norm.cdf(d1)
    Nd2 = stats.norm.cdf(d2)
    result = (s_0*Nd1) - (strike_price*math.exp(-interest_rate*partition_of_time))*Nd2
    if type=="call":
        return result
    else:
        return result*-1

def monte_carlo_cal(s_0, strike_price, volatility, interest_rate, ekspektasi_return, partition_of_time, type):
    data_temp = []
    for i in range(10):
        data_temp.append(stats.norm.ppf(random.random(), loc=ekspektasi_return , scale=volatility))

    data_result = pd.DataFrame(data_temp, columns=['return'])
    data_result['price'] = s_0 * (1+data_result['return'])
    if type == "call":
        data_result['simulated_call_c'] = data_result["price"].apply(lambda x: math.exp(-interest_rate*partition_of_time) * max(x-strike_price, 0))
    else:
        data_result['simulated_call_c'] = data_result["price"].apply(lambda x: math.exp(-interest_rate*partition_of_time) * max(strike_price-x, 0))

    return data_result.simulated_call_c.mean()

def handle_uploaded_file(f, name_file):
    with open('file_upload/'+name_file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def sub_calculation(data, partition_of_time):
    data['return'] = np.log(1+data.pct_change().fillna(0))
    data['variansi'] = (data['return']-data['return'].mean())**2
    variansi =(data.variansi.sum())/(data.shape[0]-1)
    volatility =(1/math.sqrt(partition_of_time)) * math.sqrt(variansi)
    
    return volatility, data['return'].mean()

@csrf_protect
def calculate(request):
    data_user = User.objects.order_by('-last_login').first()
    if request.method == 'POST':
        
        handle_uploaded_file(request.FILES['datasetfile'],request.FILES['datasetfile'].name)
        
        # soca black scholes and monte carlo calculation
        s_0 = float(request.POST['stock_price'])
        strike_price = float(request.POST['strike_price'])
        partition_of_time = float(request.POST['partition_of_time'])
        iteration = int(request.POST['iteration'])
        option_type = request.POST['option_type']
        interest_rate = float(request.POST['interest_rate'])
        time_exp_date = request.POST['time_exp_date']
        
        volatility, ekspektasi_return = sub_calculation(pd.read_csv("file_upload/"+request.FILES['datasetfile'].name),partition_of_time)
        
        data_calc = trx_calculation.objects.create(
            date_simulate=datetime.now(),
            option_type=option_type,
            stock_price=s_0,
            strike_price=strike_price,
            interest_rate=interest_rate,
            return_expectation=ekspektasi_return,
            time_exp_date=time_exp_date,
            iteration=iteration,
            volatility=volatility,
            partition_of_time=partition_of_time,
            user_id=data_user
        )
        
        for number in range(iteration):
            if option_type=="call_put":
                result_bs_call = black_scholes_cal(s_0, strike_price, partition_of_time, volatility, interest_rate, "call")
                result_bs_put = black_scholes_cal(s_0, strike_price, partition_of_time, volatility, interest_rate, "put")
                result_mc_call = monte_carlo_cal(s_0, strike_price, volatility, interest_rate, ekspektasi_return, partition_of_time, "call")
                result_mc_put = monte_carlo_cal(s_0, strike_price, volatility, interest_rate, ekspektasi_return, partition_of_time, "put")
                trx_result.objects.create(trx_calculation_id=data_calc, 
                                          type_calculation="Black Scholes", 
                                          call_prediction=result_bs_call, 
                                          put_prediction=result_bs_put)
                trx_result.objects.create(trx_calculation_id=data_calc, 
                                          type_calculation="Monte Carlo", 
                                          call_prediction=result_mc_call, 
                                          put_prediction=result_mc_put)
            elif option_type=="call":
                result_bs = black_scholes_cal(s_0, strike_price, partition_of_time, volatility, interest_rate, option_type)
                result_mc = monte_carlo_cal(s_0, strike_price, volatility, interest_rate, ekspektasi_return, partition_of_time, option_type)
                trx_result.objects.create(trx_calculation_id=data_calc, 
                                          type_calculation="Black Scholes", 
                                          call_prediction=result_bs)
                trx_result.objects.create(trx_calculation_id=data_calc, 
                                          type_calculation="Monte Carlo", 
                                          call_prediction=result_mc)
            else:
                result_bs = black_scholes_cal(s_0, strike_price, partition_of_time, volatility, interest_rate, option_type)
                result_mc = monte_carlo_cal(s_0, strike_price, volatility, interest_rate, ekspektasi_return, partition_of_time, option_type)
                trx_result.objects.create(trx_calculation_id=data_calc, 
                                          type_calculation="Black Scholes", 
                                          put_prediction=result_bs)
                trx_result.objects.create(trx_calculation_id=data_calc, 
                                          type_calculation="Monte Carlo", 
                                          put_prediction=result_mc)
            
    return HttpResponseRedirect(reverse('result_page'))