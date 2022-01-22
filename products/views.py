from django.views import generic

from .models import Book
from .utils import exact_filter, range_filter, order_by_query


class ProductsView(generic.ListView):
    paginate_by = 15
    template_name = 'products/all_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        query_set = Book.objects.all()

        query_set = exact_filter(self, query_set, 'full_name', 'author')
        query_set = exact_filter(self, query_set, 'name', 'category')
        query_set = exact_filter(self, query_set, 'name', 'subcategory')
        query_set = exact_filter(self, query_set, 'name', 'publisher')

        query_set = range_filter(self, query_set, 'price')
        query_set = range_filter(self, query_set, 'year')
        query_set = range_filter(self, query_set, 'pages')

        query_set = order_by_query(self, query_set)
        return query_set


class ProductByIdView(generic.DetailView):
    model = Book
    template_name = 'products/product.html'
