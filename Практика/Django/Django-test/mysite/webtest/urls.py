from django.conf.urls import url
# импорт из локального приложения (webtest). '.' - из текущей директории (где находится сам файл)
from . import views
urlpatterns=[
    # '^' - обозначает начало. $ - обозначает конец
    url(r'^$', views.index, name='index')
]