from django.db import models

# Create your models here.


class Transaction(models.Model):
    name = models.CharField(max_length=10000000)
    email = models.EmailField(max_length=10000000)
    deb_amt = models.IntegerField()
    cr_amt = models.IntegerField()
    acc_bal = models.IntegerField()


class customerdetails(models.Model):
    name = models.CharField(max_length=1000000)
    email = models.EmailField(max_length=1000000)
    curr_bal = models.IntegerField()
