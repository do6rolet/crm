from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm



def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'customers': customers, 'orders': orders, 'total_orders': total_orders,
               'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'orders_count': orders_count}
    return render(request, 'accounts/customer.html', context)


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            url = '/customer/' + str(pk) + '/'
            return redirect(url)
    context = {'formset': formset, }
    return render(request, 'accounts/order_form_customer.html', context)


def updateOrder(request, whereis, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            if whereis == 'customer':
                url = '/customer/' + str(order.customer.id) + '/'
                return redirect(url)
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)



def deleteOrder(request, whereis, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    if whereis == 'customer':
        url = '/customer/' + str(order.customer.id) + '/'
        return redirect(url)
    return redirect('/')





