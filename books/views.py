from django.http import HttpResponse

def book_post(request):
    return HttpResponse("Сегодня мы обсуждаем книгу 'Исскуство войны' Сунь-Цзы.")
