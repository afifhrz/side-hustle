from django.db import models
from datetime import datetime
from calculation.models import trx_calculation

# Create your models here.
class trx_result(models.Model):
    trx_calculation_id = models.ForeignKey(trx_calculation, on_delete=models.RESTRICT, db_column="TRX_CALCULATION_ID")
    type_calculation = models.CharField(max_length=30, db_column="TYPE_CALCULATION")
    call_prediction = models.DecimalField(db_column="CALL_PREDICTION", blank=True, null=True, decimal_places=4, max_digits=20) 
    put_prediction = models.DecimalField(db_column="PUT_PREDICTION", blank=True, null=True, decimal_places=4, max_digits=20) 

    class Meta:
        db_table = 'TRX_RESULT'