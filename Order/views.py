from django.shortcuts import render
from .models import Order

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
            order = Order.objects.create(id=order_id, client=client_name, is_ready=True)
            order.save()
            alert = None

    else:
        alert = None

    orders = Order.objects.all()
    return render(request, 'sellersPage.html', {'orders': orders, 'alert': alert})
