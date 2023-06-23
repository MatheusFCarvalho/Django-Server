from django.urls import path
from .views import SellersPage, ConfirmOrder

app_name = 'order'

urlpatterns = [
    path('sellers/', SellersPage.as_view(), name='create'),
    path('confirm/', ConfirmOrder.as_view(), name='confirm'),
]
