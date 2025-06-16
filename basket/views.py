from django.shortcuts import render, redirect, get_object_or_404
from .models import Basket
from .forms import BasketForm

def basket_list(request):
    orders = Basket.objects.all()
    return render(request, 'basket/basket_list.html', {'orders': orders})

def basket_create(request):
    if request.method == 'POST':
        form = BasketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = BasketForm()
    return render(request, 'basket/basket_form.html', {'form': form})

def basket_update(request, pk):
    order = get_object_or_404(Basket, pk=pk)
    if request.method == 'POST':
        form = BasketForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = BasketForm(instance=order)
    return render(request, 'basket/basket_form.html', {'form': form})

def basket_delete(request, pk):
    order = get_object_or_404(Basket, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('basket_list')
    return render(request, 'basket/basket_confirm_delete.html', {'order': order})
