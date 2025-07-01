from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    GENRE_CHOICES = [
        ('horror', 'Ужасы'),
        ('melodrama', 'Мелодрама'),
        ('boevic', 'Боевик'),
        ('fantastica', 'Фантастика')
        # можно расширить
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    release_date = models.DateField()
    rating = models.FloatField(default=0)
    tags = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
