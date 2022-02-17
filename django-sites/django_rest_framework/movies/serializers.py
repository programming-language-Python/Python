from rest_framework import serializers

from .models import Movie, Review, Rating, Actor


# Сериализаторы нужны для того, чтобы преобразовывать
# типы данных python в JSON и из JSON в типы данных python


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""

    # data - это QuerySet
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """"Вывод рекурсивно children"""

    # value - это значение одной записи из БД
    def to_representation(self, value):
        # ищет всех детей завязанных на нашем отзыве
        serializers = self.parent.parent.__class__(value, context=self.context)
        return serializers.data


class ActorListSerializer(serializers.ModelSerializer):
    """Вывод списка актёров и режиссёров"""

    class Meta:
        model = Actor
        fields = ("id", "name", "image")


class ActorDetailSerializer(serializers.ModelSerializer):
    """Вывод полного описания актёра или режиссёра"""

    class Meta:
        model = Actor
        fields = "__all__"


class MovieListSerializer(serializers.ModelSerializer):
    """Список фильмов"""
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Movie
        # поля которые хотим сериализовать
        fields = ("id", "title", "tagline", "category",
                  "rating_user", "middle_star")


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""
    # добавили поле children. рекурсивный вывод вложенных записей
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("name", "text", "children",)


class MovieDetailSerializer(serializers.ModelSerializer):
    """Полный фильм"""
    # slug_field - выводит не id, а поле name во внешнем ключе.
    # read_only=True - поле для чтения
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    # many=True т.к. связь ManyToMany
    directors = ActorListSerializer(
        read_only=True, many=True)
    actors = ActorListSerializer(
        read_only=True, many=True)
    genres = serializers.SlugRelatedField(
        slug_field="name", read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        # выводит все поля, пишем тот который хотим исключить
        exclude = ("draft",)


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователя"""

    class Meta:
        model = Rating
        fields = ("star", "movie")

    # validated_data - это данные которые мы передаёи в наш сериадизатор от клиенской стороны
    def create(self, validated_data):
        # если rating = ... то он будет кортежем
        # если как ниже, то в rating будет объект, а в _ булево значение
        rating, _ = Rating.objects.update_or_create(ip=validated_data.get('ip', None),
                                                    movie=validated_data.get(
                                                        'movie', None),
                                                    defaults={
                                                        'star': validated_data.get("star")}
                                                    )
        return rating
