from django.db import models
import datetime

# Create your models here.
class master_link(models.Model):
    URI_link = models.CharField(max_length=500, db_column="URI_LINK")
    date_created = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), blank=True, db_column="DATE_CREATED")

    class Meta:
        db_table = 'BBCSCRAP_MASTERLINK'
        
class detail_link(models.Model):
    title = models.CharField(max_length=1000, db_column="TITLE")
    description = models.CharField(max_length=10000, db_column="DESCRIPTION")
    date_created = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), blank=True, db_column="DATE_CREATED")
    link_id = models.ForeignKey(master_link, on_delete=models.RESTRICT, db_column="LINK_ID")

    class Meta:
        db_table = 'BBCSCRAP_DETAILLINK'
