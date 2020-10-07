from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('products', views.products, name='products'),
    path('customer/<str:pk>/', views.customer_details, name='customer_details'),
    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('delete_order/<str:whereis>/<str:pk>/', views.deleteOrder, name='delete_order'),
    path('update_order/<str:whereis>/<str:pk>/', views.updateOrder, name='update_order'),

]