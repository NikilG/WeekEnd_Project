from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#model to create/store news feed Info
class Newsfeed(models.Model):
    by = models.CharField(max_length=256,null=False)
    title = models.CharField(max_length=256,null=False, db_index = True)
    type = models.CharField(max_length=256,null=False)
    score = models.IntegerField()
    url = models.CharField(max_length=256,null=True)
    computedsentiment = models.CharField(max_length=256,null=False, default="", editable=False)
    time = models.CharField(max_length=256,null=False)
 