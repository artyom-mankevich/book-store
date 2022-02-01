from django.db.models import QuerySet, Q
from django.views.generic.base import View


def exact_filter(view: View, query_set: QuerySet,
                 field_name: str, foreign_key: str = None):
    parameters: list = view.request.GET.getlist(foreign_key)
    if parameters:
        if foreign_key:
            lookup_str = foreign_key + '__' + field_name
        else:
            lookup_str = field_name

        if len(parameters) > 1:
            query_set = query_set.filter(get_q_obj(parameters, lookup_str))
        else:
            query_set = query_set.filter(**{lookup_str: parameters[0]})
    return query_set


def get_q_obj(parameters: list, lookup_str: str):
    q = Q()
    for p in parameters:
        q |= Q(**{lookup_str: p})
    return q


def range_filter(view: View, query_set: QuerySet, field_name: str):
    start = view.request.GET.get(field_name + '_from')
    end = view.request.GET.get(field_name + '_to')

    if start is not None and end is not None:
        field_name += '__range'
        query_set = query_set.filter(**{field_name: (start, end)})
    elif start is not None:
        field_name += '__gte'
        query_set = query_set.filter(**{field_name: start})
    elif end is not None:
        field_name += '__lte'
        query_set = query_set.filter(**{field_name: end})
    return query_set


def order_by_query(view: View, query_set: QuerySet):
    allowed_orders = ('price', 'rating', 'pages', 'year')
    ordering_by: str = view.request.GET.get('order')

    if ordering_by:
        order_field = ordering_by[:ordering_by.find(':')]
        if order_field in allowed_orders:
            descending = ordering_by.endswith(':desc')
            if descending:
                order_field = '-' + order_field
            return query_set.order_by(*(order_field,))

    return query_set.order_by('-year')


def book_directory_path(instance, filename):
    """Returns MEDIA_ROOT/books/book.isbn/filename"""
    return 'books/{0}/{1}'.format(instance.book.isbn, filename)


def author_directory_path(instance, filename):
    """Returns MEDIA_ROOT/authors/author.slug/filename"""
    return 'authors/{0}/{1}'.format(instance.slug, filename)
