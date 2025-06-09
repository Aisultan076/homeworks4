from django.db import models

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