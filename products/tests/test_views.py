from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized

from .factories import BookFactory, AuthorFactory, CategoryFactory, SubcategoryFactory, PublisherFactory


class ProductsListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        products_number = 17

        cls.author = AuthorFactory()
        cls.category = CategoryFactory()
        cls.subcategory = SubcategoryFactory()
        cls.publisher = PublisherFactory()

        for i in range(products_number):
            BookFactory(author=cls.author, category=cls.category,
                        subcategory=cls.subcategory, publisher=cls.publisher,
                        title=str(i), slug=str(i))

    def test_view_all_products_url_exists(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_view_all_products_url_by_name(self):
        response = self.client.get(reverse('products:products'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_15(self):
        response = self.client.get(reverse('products:products') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'])
        self.assertEqual(len(response.context['page_obj']), 2)

    @parameterized.expand([('author', 'full_name'),
                           ('publisher', 'name'),
                           ('category', 'name'),
                           ('subcategory', 'name')])
    def test_query_string_exact_filter(self, foreign_key_name, field_name: str):
        """
        Tests for query string exact filtering.
        Query string example: /products/?author=John Smith
        Arguments:
            foreign_key_name - foreign key field in Book model, example: author
            field_name - foreign key model's field that is basis for filtering, example: full_name
        """
        fk = getattr(self, foreign_key_name)
        fk_field = getattr(fk, field_name)
        query_string = f"?{foreign_key_name}=" + fk_field
        response = self.client.get(reverse('products:products') + query_string)
        self.assertEqual(response.status_code, 200)
        for i in response.context['page_obj']:
            item_fk = getattr(i, foreign_key_name)
            item_fk_field = getattr(item_fk, field_name)
            self.assertEqual(fk_field, item_fk_field)

    @parameterized.expand([('price', 10, 20),
                           ('year', 2000, 2015),
                           ('pages', 200, 280)])
    def test_query_string_range_filter(self, field_name, start, end):
        """
        Tests for query string range filtering.
        Query string example: /products/?price_from=10&price_to=50
        Arguments:
            field_name - Book's field name, example: price
            start - Filtering lower bound
            end - Filtering higher bound
        """
        query_string = f"?{field_name}_from={start}&{field_name}_to={end}"
        response = self.client.get(reverse('products:products') + query_string)
        self.assertEqual(response.status_code, 200)
        for i in response.context['page_obj']:
            item_field = getattr(i, field_name)
            self.assertTrue(start < item_field < end)

    @parameterized.expand([('price', 'asc'),
                           ('price', 'desc'),
                           ('rating', 'asc'),
                           ('rating', 'desc'),
                           ('pages', 'asc'),
                           ('pages', 'desc'),
                           ('year', 'asc'),
                           ('year', 'desc')])
    def test_query_string_order(self, field_name, order):
        query_string = f"?order={field_name}:{order}"
        response = self.client.get(reverse('products:products') + query_string)
        self.assertEqual(response.status_code, 200)
        prev_value = None
        for i in response.context['page_obj']:
            field_value = getattr(i, field_name)
            if prev_value is not None:
                if order == 'asc':
                    self.assertTrue(prev_value <= field_value)
                else:
                    self.assertTrue(prev_value >= field_value)
            else:
                prev_value = field_value

    def test_correct_template(self):
        response = self.client.get(reverse('products:products'))
        self.assertTemplateUsed(response, 'products/all_products.html')


class ProductDetailsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = BookFactory()

    def test_product_details_url_exists(self):
        response = self.client.get(f'/products/{self.book.author.slug}/{self.book.slug}')
        self.assertEqual(response.status_code, 200)

    def test_product_details_url_by_name(self):
        response = self.client.get(
            reverse('products:product details',
                    kwargs={'author': self.book.author.slug, 'slug': self.book.slug}))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(
            reverse('products:product details',
                    kwargs={'author': self.book.author.slug, 'slug': self.book.slug}))
        self.assertTemplateUsed(response, 'products/product.html')
