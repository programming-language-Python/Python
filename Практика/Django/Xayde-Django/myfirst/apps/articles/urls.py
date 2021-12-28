from django.urls import path
from . import views
# . - из текущего пакета
urlpatterns = [
    path('',views.index, name='index')
]