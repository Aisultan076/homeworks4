from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models


def book_list(request):
    books = models.Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(models.Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})



def book_post(request):
    return HttpResponse("Сегодня мы обсуждаем книгу 'Исскуство войны' Сунь-Цзы.")