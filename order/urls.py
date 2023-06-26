from django.urls import path
from .views import SellersPage, ConfirmOrder, MasterPage, CreateOrder

app_name = 'order'

urlpatterns = [
    path('', SellersPage, name='create'),
    path('confirm/', ConfirmOrder, name='confirm'),
    path('master/', MasterPage, name='confirm'),
    path('create/', CreateOrder, name='confirm'),
]
