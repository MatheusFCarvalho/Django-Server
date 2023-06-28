from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm
from django.http import HttpResponse

@login_required
def SellersPage(request):
    user = request.user
    print(request.user)
    print(request.user.id)
    print(request.user.trustly)
    orders = Order.objects.filter(seller_id=user.id)
    return render(request, 'sellersPage.html', {'orders': orders, 'user':user})
from django.contrib.auth.decorators import login_required

@login_required
def MasterPage(request):
    user = request.user

    if user.trustly:
        orders = Order.objects.all()
        return render(request, 'masterPage.html', {'orders': orders, 'user': user})
    else:
        return HttpResponse("Acesso não autorizado.")  # Ou redirecionar para uma página de erro, por exemplo.



def ConfirmOrder(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order, created = Order.objects.get_or_create(id=order_id)
            order.is_ready = True
            order.save()

    orders = Order.objects.all()
    return render(request, 'confirmOrder.html', {'orders': orders})
    return render(request, 'masterPage.html', {'orders': orders})