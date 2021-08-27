from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(max_length=100, null=True)
    is_best_selling = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} {self.rating}'
