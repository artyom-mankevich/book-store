from django.shortcuts import render
from django.views import generic

from .models import Book, Author
from .utils import exact_filter, range_filter, order_by_query


class ProductsView(generic.ListView):
    paginate_by = 15
    template_name = 'products/all_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        query_set = Book.objects.select_related('author', 'category',
                                                'subcategory', 'publisher').all()

        query_set = exact_filter(self, query_set, 'full_name', 'author')
        query_set = exact_filter(self, query_set, 'name', 'category')
        query_set = exact_filter(self, query_set, 'name', 'subcategory')
        query_set = exact_filter(self, query_set, 'name', 'publisher')

        query_set = range_filter(self, query_set, 'price')
        query_set = range_filter(self, query_set, 'year')
        query_set = range_filter(self, query_set, 'pages')

        query_set = order_by_query(self, query_set)
        return query_set


class ProductDetails(generic.DetailView):
    model = Book
    template_name = 'products/product.html'

    def get_queryset(self):
        query_set = Book.objects \
            .select_related('author',
                            'category',
                            'subcategory',
                            'publisher') \
            .filter(slug=self.kwargs['slug'],
                    author__slug=self.kwargs['author'])
        return query_set


class AuthorDetails(generic.DetailView):
    model = Author
    template_name = 'products/author.html'

    def get(self, request, *args, **kwargs):
        author = Author.objects.get(slug=self.kwargs['slug'])
        author_books = Book.objects.filter(author=author).order_by('-year')[:5]
        author_categories: list = []
        for book in author_books:
            author_categories.append(book.category)
        return render(request, 'products/author.html', context={
            'author': author,
            'author_books': author_books,
            'author_categories': author_categories
        })


class PublisherDetails(generic.DetailView):
    pass
