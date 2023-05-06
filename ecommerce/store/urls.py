from django.urls import path
from . import views

urlpatterns = [
    # Store main page

    path('', views.store, name='store'),

    # Individual product
    path('product/<str:product_slug>/', views.product_info, name='product-info'),

    # Individual category
    path('search/<str:category_slug>/', views.list_category, name='list-category'),

]
