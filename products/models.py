from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from products.utils import book_directory_path


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, verbose_name="Country that is associated with the author", null=True,
                               blank=True)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(editable=False, max_digits=4, decimal_places=2, null=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('products:author details', kwargs={'slug': self.slug})

    def __str__(self):
        return ' '.join((str(self.id), self.full_name))


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return ' '.join((str(self.id), self.name))


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return ' '.join((str(self.id), self.name))


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    rating = models.DecimalField(editable=False, max_digits=4, decimal_places=2, null=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('products:publisher details', kwargs={'slug': self.slug})

    def __str__(self):
        return ' '.join((str(self.id), self.name))


class BookImage(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=book_directory_path)

    def __str__(self):
        return ' '.join((str(self.id), self.book.title))


class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=20, unique=True,
                            verbose_name="International Standard Book Number")

    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    main_image = models.ForeignKey(BookImage, on_delete=models.SET_NULL, null=True, related_name='+', blank=True)

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    HARD = 'H'
    SOFT = 'S'
    COVER_CHOICES = [
        (HARD, "Hard"),
        (SOFT, "Soft"),
    ]
    cover = models.CharField(max_length=1, choices=COVER_CHOICES,
                             verbose_name="a type of book cover")

    dimensions = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=13, decimal_places=4)
    year = models.SmallIntegerField()
    pages = models.SmallIntegerField()
    available_count = models.SmallIntegerField()
    rating = models.DecimalField(editable=False, max_digits=4, decimal_places=2, null=True)

    def get_absolute_url(self):
        return reverse('products:product details', kwargs={'author': self.author.slug, 'slug': self.slug})

    def __str__(self):
        return ' '.join((self.isbn, self.title))
