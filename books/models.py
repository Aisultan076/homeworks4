from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Напишите название книги')
    author = models.CharField(max_length=100, verbose_name='Напишите автора')
    description = models.TextField()
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    cover_image = models.URLField()
    audio_embed = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'


class Review(models.Model):
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', verbose_name='выберите книгу')
    text = models.TextField(verbose_name='Напишите отзыв')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Оценка должна быть от 1 до 5."),
            MaxValueValidator(5, message="Оценка должна быть от 1 до 5.")
        ]
    )

    def __str__(self):
        return f"Отзыв от {self.author} на {self.choice_book}"

    class Meta:
        verbose_name='отзыв'
        verbose_name_plural='отзывы'