from django.db import models

from django.conf import settings

User = settings.AUTH_USER_MODEL

class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)