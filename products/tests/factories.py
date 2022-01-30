import factory
from faker import Faker

from products.models import Book, Author, Category, Subcategory, Publisher

FAKE = Faker('en_US')


def create_slug(title: str):
    return title.lower().replace(' ', '_')


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    full_name = FAKE.name()
    slug = create_slug(full_name)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('company')


class SubcategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subcategory

    name = factory.Faker('company')
    category = factory.SubFactory(CategoryFactory)


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publisher

    name = FAKE.company()
    slug = create_slug(name)


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    isbn = factory.Faker('isbn10')

    author = factory.SubFactory(AuthorFactory)
    category = factory.SubFactory(CategoryFactory)
    subcategory = factory.SubFactory(SubcategoryFactory)
    publisher = factory.SubFactory(PublisherFactory)

    title = FAKE.name()
    price = 12
    slug = create_slug(title)
    cover = "H"
    year = 1890
    pages = 230
    available_count = 1
