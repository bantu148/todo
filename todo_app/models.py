from django.db import models


# Create your models here.
class todoitems(models.Model):
    content = models.TextField()