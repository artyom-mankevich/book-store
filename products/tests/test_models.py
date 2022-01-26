from django.test import TestCase

from .factories import BookFactory, AuthorFactory, PublisherFactory


class BookTestCase(TestCase):
    def setUp(self):
        self.book = BookFactory.create()

    def test_get_absolute_url(self):
        expected_url = f"/products/{self.book.author.slug}/{self.book.slug}"
        self.assertEqual(self.book.get_absolute_url(), expected_url)


class AuthorTestCase(TestCase):
    def setUp(self):
        self.author = AuthorFactory.create()

    def test_get_absolute_url(self):
        expected_url = f"/products/{self.author.slug}"
        self.assertEqual(self.author.get_absolute_url(), expected_url)


class PublisherTestCase(TestCase):
    def setUp(self):
        self.publisher = PublisherFactory.create()

    def test_get_absolute_url(self):
        expected_url = f"/products/{self.publisher.slug}"
        self.assertEqual(self.publisher .get_absolute_url(), expected_url)
