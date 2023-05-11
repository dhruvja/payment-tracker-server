from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.apiOverview,name="apiOverview"),
    path('all-payments', views.getAllPayments, name = 'allPayments'),
    path('submit-payment', views.submitPayment, name = 'submitPayment'),
]