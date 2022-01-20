from django.contrib.auth.models import AbstractUser
from django.db import models

from products.models import Book
from store_project import settings
from .utils import user_directory_path


class CustomUser(AbstractUser):
    bio = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.username


class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    WATCH_LATER = 'LATER'
    READ = 'READ'
    TYPE_CHOICES = [
        (WATCH_LATER, 'Watch later'),
        (READ, 'Already read'),
    ]
    type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    date = models.DateField(auto_now=True)
