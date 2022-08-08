from django.db import models
from accounts.models import CustomUser
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100, default=' nameless')
    author = models.CharField(max_length=100)
    publisher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    info = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('book_list')

    def __str__(self):
        return self.title
