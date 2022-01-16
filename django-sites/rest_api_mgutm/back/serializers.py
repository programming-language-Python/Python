from rest_framework import serializers

from .models import Actor


# Сериализаторы нужны для того, чтобы преобразовывать
# типы данных python в JSON и из JSON в типы данных python

class ActorListSerializer(serializers.ModelSerializer):
    """Вывод списка актёров и режиссёров"""

    class Meta:
        model = Actor
        fields = ("id", "name")


class ActorDetailSerializer(serializers.ModelSerializer):
    """Вывод полного описания актёра или режиссёра"""

    class Meta:
        model = Actor
        fields = "__all__"
