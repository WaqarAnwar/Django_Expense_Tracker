from django.db import models
from django.utils import timezone

class Entry(models.Model):
    amount = models.FloatField()
    description = models.CharField(max_length=1000)

    OPTIONS_CHOICES = (('cash_in','Cash In'), ('cash_out', 'Cash Out'))
    options = models.CharField(choices=OPTIONS_CHOICES, max_length=20, null=True)
    date_time = models.DateTimeField(default=timezone.now)
