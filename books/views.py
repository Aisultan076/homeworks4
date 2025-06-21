from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import title
from django.core.paginator import Paginator
from . import models


def book_list(request):
    query = request.GET.get('q')
    books = models.Book.objects.all()
    book_queryset = models.Book.objects.all()
    if query:
        books = books.filter(title__icontains=query)
        book_queryset = book_queryset.filter(title__icontains=query)

    paginator = Paginator(book_queryset, 5)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)

    return render(request, 'book/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(models.Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})



def book_post(request):
    return HttpResponse("Сегодня мы обсуждаем книгу 'Исскуство войны' Сунь-Цзы.")


def book_detail(request, pk):
    book = get_object_or_404(models.Book, pk=pk)
    reviews = book.reviews.all()
    average_mark = reviews.aggregate(models.Avg('mark'))['mark__avg']
    return render(request, 'book_detail.html', {
        'book': book,
        'reviews': reviews,
        'average_mark': average_mark
    })