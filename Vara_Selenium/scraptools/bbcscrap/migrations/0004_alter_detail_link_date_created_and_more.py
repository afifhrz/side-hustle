# Generated by Django 4.1 on 2023-03-14 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbcscrap', '0003_alter_master_link_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail_link',
            name='date_created',
            field=models.DateTimeField(blank=True, db_column='DATE_CREATED', default='2023-03-14 10:07:38'),
        ),
        migrations.AlterField(
            model_name='master_link',
            name='date_created',
            field=models.DateTimeField(blank=True, db_column='DATE_CREATED', default='2023-03-14 10:07:38'),
        ),
    ]