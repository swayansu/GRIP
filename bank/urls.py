from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customer', views.customer, name='customer'),
    path('transactions', views.transactions, name='transaction_details')
]
