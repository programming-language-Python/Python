from django.db import models
from rest_framework import generics, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.response import Response
# from rest_framework.views import APIView

from .models import Movie, Actor
from movies.serializers import MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializer, \
    CreateRatingSerializer, ActorListSerializer, ActorDetailSerializer
from movies.service import get_client_ip, MovieFilter, PaginationMovies


# через ViewSet
# ReadOnlyModelViewSet - позволяет выводить список фильмов и полный фильм
class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка фильмов"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter
    pagination_class = PaginationMovies

    def get_queryset(self):
        # Способ №2. Убирает дубли записей
        movies = Movie.objects.filter(draft=False).annotate(
            # ratings__ip - обращается к полю movie (с помощью related_name) у модели Ratings
            # и у данной модели обращаемся к полю ip
            # then=True - если такая запись найдётся то выведет True
            rating_user=models.Count("ratings", filter=models.Q(
                ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / \
                        models.Count(models.F('ratings'))
        )
        return movies

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        elif self.action == 'retrieve':
            return MovieDetailSerializer


class ReviewCreateViewSet(viewsets.ModelViewSet):
    """Добавление отзыва к фильму"""
    serializer_class = ReviewCreateSerializer


class AddStarRatingViewSet(viewsets.ModelViewSet):
    """Добавление рейтинга фильму"""
    serializer_class = CreateRatingSerializer

    # в CreateAPIView классе существует метод perform_create.
    # в save можем указывать параметры которые дополнительно хотим указать при сохранении
    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


class ActorsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка актёров"""
    queryset = Actor.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ActorListSerializer
        elif self.action == 'retrieve':
            return ActorDetailSerializer

# class MovieListView(APIView):
#     """Вывод списка фильмов"""
#
#     def get(self, request):
#         # Способ №1
#         # movies = Movie.objects.filter(draft=False).annotate(
#         #     # ratings__ip - обращается к полю movie (с помощью related_name) у модели Ratings
#         #     # и у данной модели обращаемся к полю ip
#         #     # then=True - если такая запись найдётся то выведет True
#         #     rating_user=models.Case(models.When(ratings__ip=get_client_ip(request), then=True),
#         #                             default=False,
#         #                             output_field=models.BooleanField())
#         # )
#         # Способ №2. Убирает дубли записей
#         movies = Movie.objects.filter(draft=False).annotate(
#             # ratings__ip - обращается к полю movie (с помощью related_name) у модели Ratings
#             # и у данной модели обращаемся к полю ip
#             # then=True - если такая запись найдётся то выведет True
#             rating_user=models.Count("ratings", filter=models.Q(
#                 ratings__ip=get_client_ip(request)))
#         ).annotate(
#             middle_star=models.Sum(models.F('ratings__star')) / \
#                         models.Count(models.F('ratings'))
#         )
#
#         # заносим работу сериализатора, передаёт QuerySet
#         # и many=True он говорит что у нас будет несколько записей
#         serializer = MovieListSerializer(movies, many=True)
#         return Response(serializer.data)
#
#
# class MovieDetailView(APIView):
#     """Вывод фильма"""
#
#     def get(self, request, pk):
#         movie = Movie.objects.get(id=pk, draft=False)
#         serializer = MovieDetailSerializer(movie)
#         return Response(serializer.data)
#
#
# class ReviewCreateView(APIView):
#     """Добавление отзыва к фильму"""
#
#     def post(self, request):
#         # request.data. data - это то что содержится в клиенском запросе
#         review = ReviewCreateSerializer(data=request.data)
#         if review.is_valid():
#             review.save()
#         return Response(status=201)
#
#
# class AddStarRatingView(APIView):
#     """Добавление рейтинга фильму"""
#
#     def post(self, request):
#         serializer = CreateRatingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(ip=get_client_ip(request))
#             return Response(status=201)
#         else:
#             return Response(status=400)
#
#
# # generic (дженерик) классы (будем использовать ListAPIView, RetrieveAPIView) - с лёгкостью можем описывать логику которую хотим вывести
# # через generics.ListAPIView
# class MovieListView(generics.ListAPIView):
#     """Вывод списка фильмов"""
#     serializer_class = MovieListSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = MovieFilter
#     # какие права доступа должны быть у пользователя чтобы просмотреть данный url
#     # можно создавать свои permission
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         # Способ №2. Убирает дубли записей
#         movies = Movie.objects.filter(draft=False).annotate(
#             # ratings__ip - обращается к полю movie (с помощью related_name) у модели Ratings
#             # и у данной модели обращаемся к полю ip
#             # then=True - если такая запись найдётся то выведет True
#             rating_user=models.Count("ratings", filter=models.Q(
#                 ratings__ip=get_client_ip(self.request)))
#         ).annotate(
#             middle_star=models.Sum(models.F('ratings__star')) / \
#                         models.Count(models.F('ratings'))
#         )
#         return movies
#
#
# # через generics.RetrieveAPIView
# # RetrieveAPIView - для вывода полного описания фильма это аналог класса DetailView для Django
# class MovieDetailView(generics.RetrieveAPIView):
#     """Вывод фильма"""
#
#     queryset = Movie.objects.filter(draft=False)
#     serializer_class = MovieDetailSerializer
#
#
# # через generics.CreateAPIView
# class ReviewCreateView(generics.CreateAPIView):
#     """Добавление отзыва к фильму"""
#     serializer_class = ReviewCreateSerializer
#
#
# class AddStarRatingView(generics.CreateAPIView):
#     """Добавление рейтинга фильму"""
#     serializer_class = CreateRatingSerializer
#
#     # в CreateAPIView классе существует метод perform_create.
#     # в save можем указывать параметры которые дополнительно хотим указать при сохранении
#     def perform_create(self, serializer):
#         serializer.save(ip=get_client_ip(self.request))
#
#
# class ActorsListView(generics.ListAPIView):
#     """Вывод списка актёров"""
#     queryset = Actor.objects.all()
#     serializer_class = ActorListSerializer
#
#
# class ActorsDetailView(generics.RetrieveAPIView):
#     """Вывод актёра или режиссёра"""
#     queryset = Actor.objects.all()
#     serializer_class = ActorDetailSerializer
