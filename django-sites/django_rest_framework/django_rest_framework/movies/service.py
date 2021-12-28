from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from movies.models import Movie


class PaginationMovies(PageNumberPagination):
    page_size = 2
    max_page_size = 1000

    # данный метод говорит каким образом
    # мы будем выводить информацию о нашей пагинации
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


# определяет ip адрес пользователя
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


# FilterSet - позволяет указывать поля и дополнительную логику с помощью,
# которой мы будем фильтровать
class MovieFilter(filters.FilterSet):
    # field_name - поле по которому будем искать
    # genres - это модель, а name - это поле,
    # получается ищем по полю name (по умолчанию ищет по id)
    # lookup_expr - как поле нужно фильтровать
    # in - это вхождение
    genres = CharFilterInFilter(field_name='genres__name', lookup_expr='in')
    # RangeFilter - диапазон дат от минимального к максиальному
    year = filters.RangeFilter()

    class Meta:
        model = Movie
        # поля по которым будем фильтровать
        fields = ['genres', 'year']
