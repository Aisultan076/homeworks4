from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Basket
from .forms import BasketForm

class BasketListView(ListView):
    model = Basket
    template_name = 'basket/basket_list.html'
    context_object_name = 'orders'


class BasketCreateView(CreateView):
    model = Basket
    form_class = BasketForm
    template_name = 'basket/basket_form.html'
    success_url = reverse_lazy('basket_list')


class BasketUpdateView(UpdateView):
    model = Basket
    form_class = BasketForm
    template_name = 'basket/basket_form.html'
    success_url = reverse_lazy('basket_list')


class BasketDeleteView(DeleteView):
    model = Basket
    template_name = 'basket/basket_confirm_delete.html'
    context_object_name = 'order'
    success_url = reverse_lazy('basket_list')
