from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.surname}"


class Genre(models.Model):
    title = models.CharField(max_length=255,
                             unique=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(max_length=255, unique=True, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False)
    release = models.DateField(blank=False)
    genre = models.ManyToManyField(Genre, blank=False)

    CHOICE_RATING = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]

    rating = models.IntegerField(blank=False,
                                 validators=[MaxValueValidator(10),
                                             MinValueValidator(1)])
    views = models.PositiveIntegerField(default=0,
                                        auto_created=True)

    def __str__(self):
        return f"{self.title} - {self.author} - {self.genre} - {self.release}"

    def get_absolute_url(self):
        return reverse('slug_param', args=[self.pk])
