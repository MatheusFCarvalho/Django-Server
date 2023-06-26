from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from .models import Order
from .forms import OrderForm

def ConfirmOrder(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order, created = Order.objects.get_or_create(id=order_id)
            order.is_ready = True
            order.save()

    orders = Order.objects.all()
    return render(request, 'confirmOrder.html', {'orders': orders})

def SellersPage(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        client_name = request.POST.get('client_name', None)

        order = Order.objects.filter(id=order_id).first()

        if order:
            alert = f"Pedido {order.id} já existe. Cliente: {order.client}. Status: {'Pronto' if order.is_ready else 'Não Pronto'}"
        else:
            order = Order.objects.create(id=order_id, client=client_name, is_ready=False)
            order.save()
            alert = None

    else:
        alert = None

    orders = Order.objects.all()
    return render(request, 'sellersPage.html', {'orders': orders, 'alert': alert})



def CreateOrder(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para uma página de sucesso ou fazer outra ação desejada
    else:
        form = OrderForm()

    return render(request, 'createOrder.html', {'form': form})


def MasterPage(request):
    orders = Order.objects.all()
    return render(request, 'masterPage.html', {'orders': orders})