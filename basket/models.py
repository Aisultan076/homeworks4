from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
from books.models import Book

class Basket(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Подтвержден'),
        ('not_confirmed', 'Не подтвержден'),
    ]

    full_name = models.CharField("ФИО", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=20)
    card_number = models.CharField(
        "Номер карты",
        max_length=16,
        validators=[MinLengthValidator(16)]
    )
    books = models.ManyToManyField(Book, verbose_name="Книги")
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='not_confirmed')

    def __str__(self):
        return f"Заказ от {self.full_name}"
