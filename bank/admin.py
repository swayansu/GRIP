from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import customerdetails, Transaction

# Register your models here.
admin.site.register(customerdetails)
admin.site.register(Transaction)
