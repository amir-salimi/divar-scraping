from django.db import models

class DivarData(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    category = models.CharField(max_length=64)
    price = models.CharField(max_length=32, default="")
    rent = models.CharField(max_length=32, default="")
    deposit = models.CharField(max_length=32, default="")
