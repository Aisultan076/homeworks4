from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.db.models import Avg
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        reviews = book.reviews.all()
        average_mark = reviews.aggregate(Avg('mark'))['mark__avg']
        context['reviews'] = reviews
        context['average_mark'] = average_mark
        return context


class BookPostView(View):
    def get(self, request):
        return HttpResponse("Сегодня мы обсуждаем книгу 'Искусство войны' Сунь-Цзы.")
