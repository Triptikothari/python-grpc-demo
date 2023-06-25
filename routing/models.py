from django.db import models
from django.db.models import JSONField
from django.db import connection


class User(models.Model):
    id = models.IntegerField(db_index=True, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    groups = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_info'
