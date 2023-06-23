from django.urls import path
from .views import SellersPage, ConfirmOrder

app_name = 'order'

urlpatterns = [
    path('sellers/', SellersPage, name='create'),
    path('confirm/', ConfirmOrder, name='confirm'),
]
