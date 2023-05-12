from django.shortcuts import redirect, render

from cart.cart import Cart

from django.http import JsonResponse


# Create your views here.


def payment_success(request):

    return render(request, 'payment/payment-success.html')


def payment_failed(request):

    return render(request, 'payment/payment-failed.html')