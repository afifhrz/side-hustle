# Generated by Django 4.1 on 2022-12-07 15:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='trx_calculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_simulate', models.DateTimeField(db_column='DATE_SIMULATE', default=datetime.datetime(2022, 12, 7, 22, 4, 15, 592096))),
                ('option_type', models.CharField(db_column='OPTION_TYPE', max_length=30)),
                ('stock_price', models.IntegerField(db_column='STOCK_PRICE')),
                ('interest_rate', models.DecimalField(db_column='INTEREST_RATE', decimal_places=2, max_digits=20)),
                ('time_exp_date', models.IntegerField(db_column='TIME_EXPIRATION')),
                ('iteration', models.IntegerField(db_column='ITERATION')),
                ('volatility', models.DecimalField(db_column='VOLATILITY', decimal_places=4, max_digits=20)),
                ('user_id', models.ForeignKey(db_column='USER_ID', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TRX_CALCULATION',
            },
        ),
    ]
