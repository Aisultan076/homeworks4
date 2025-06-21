from django.shortcuts import render
from .models import Product, Tag

def product_list(request, tag_id=None):
    tags = Tag.objects.all()
    products = Product.objects.all()
    if tag_id:
        products = products.filter(tags__id=tag_id)
    return render(request, 'gadjets/product_list.html', {
        'products': products,
        'tags': tags,
        'selected_tag': int(tag_id) if tag_id else None
    })
