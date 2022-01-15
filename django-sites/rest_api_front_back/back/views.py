from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets

from back.models import Actor
from back.serializers import ActorListSerializer, ActorDetailSerializer


class ActorsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка актёров"""
    queryset = Actor.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ActorListSerializer
        elif self.action == 'retrieve':
            return ActorDetailSerializer
