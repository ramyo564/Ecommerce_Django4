from django.urls import path
from . import views

urlpatterns = [
    # Store main page

    path('', views.store, name='store'),


]
