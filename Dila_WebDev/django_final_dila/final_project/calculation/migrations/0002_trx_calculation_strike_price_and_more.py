# Generated by Django 4.1 on 2022-12-08 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trx_calculation',
            name='strike_price',
            field=models.DecimalField(db_column='STRIKE_PRICE', decimal_places=2, default=123, max_digits=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trx_calculation',
            name='date_simulate',
            field=models.DateTimeField(db_column='DATE_SIMULATE', default=datetime.datetime(2022, 12, 8, 22, 39, 6, 593282)),
        ),
        migrations.AlterField(
            model_name='trx_calculation',
            name='stock_price',
            field=models.DecimalField(db_column='STOCK_PRICE', decimal_places=2, max_digits=20),
        ),
    ]
