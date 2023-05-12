from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [

#    path('checkout-ways/', views.checkout_ways, name='checkout-ways'),

#    # Paypal 

#    path('checkout-paypal/', views.checkout_paypal, name='checkout-paypal'),

#    path('complete-order/', views.complete_order, name='complete-order'),

   # Payment process
 
   path('payment-success/', views.payment_success, name='payment-success'),

   path('payment-failed/', views.payment_failed, name='payment-failed'),

]
