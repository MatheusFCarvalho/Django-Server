from django.urls import path
from .views import SellersPage, MasterPage, ConfirmOrder

app_name = 'order'

urlpatterns = [
    path('orders/', SellersPage, name='create'),
    path('orders/master/', MasterPage, name='create'),
    # path('master/', MasterPage, name='confirm'),
    path('confirm/', ConfirmOrder, name='confirm'),
    # path('create/', CreateOrder, name='confirm'),
]
