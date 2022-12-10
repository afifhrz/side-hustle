from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class trx_calculation(models.Model):
    date_simulate = models.DateTimeField(default=datetime.now(), db_column="DATE_SIMULATE")
    option_type = models.CharField(max_length=30, db_column="OPTION_TYPE")
    stock_price = models.DecimalField(db_column="STOCK_PRICE", decimal_places=4, max_digits=20) 
    strike_price = models.DecimalField(db_column="STRIKE_PRICE", decimal_places=4, max_digits=20) 
    interest_rate = models.DecimalField(db_column="INTEREST_RATE", decimal_places=4, max_digits=20) 
    return_expectation = models.DecimalField(db_column="RETURN_EXPECTATION", decimal_places=4, max_digits=20) 
    time_exp_date = models.IntegerField(db_column="TIME_EXPIRATION")
    iteration = models.IntegerField(db_column="ITERATION")
    partition_of_time = models.DecimalField(db_column="PARTITION_OF_TIME", decimal_places=4, max_digits=20) 
    volatility = models.DecimalField(db_column="VOLATILITY", decimal_places=4, max_digits=20)
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, db_column="USER_ID")

    class Meta:
        db_table = 'TRX_CALCULATION'