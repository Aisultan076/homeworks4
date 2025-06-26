from django.views.generic import ListView
from django.shortcuts import render
from .models import Product, Tag

class ProductListView(ListView):
    model = Product
    template_name = 'gadjets/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['selected_tag'] = int(self.kwargs.get('tag_id')) if self.kwargs.get('tag_id') else None
        return context
