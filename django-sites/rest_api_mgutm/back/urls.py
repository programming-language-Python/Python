from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# через ViewSet
urlpatterns = format_suffix_patterns([
    path("actor/", views.ActorsViewSet.as_view({'get': 'list'})),
    path("actors/<int:pk>", views.ActorsViewSet.as_view({'get': 'retrieve'})),
])
