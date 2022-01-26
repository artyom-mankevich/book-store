import factory

from products.models import Book, Author, Category, Subcategory, Publisher


def create_slug(title: str):
    return title.lower().replace(' ', '_')


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    full_name = factory.Faker('name')
    slug = 'some_test_slug'


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

    name = factory.Faker('name')
    slug = 'test_slug'


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    isbn = factory.Faker('isbn10')

    author = factory.SubFactory(AuthorFactory)
    category = factory.SubFactory(CategoryFactory)
    subcategory = factory.SubFactory(SubcategoryFactory)
    publisher = factory.SubFactory(PublisherFactory)

    title = "Test title"
    price = 12
    slug = 'test_title'
    cover = "H"
    year = 1890
    pages = 230
    available_count = 1
