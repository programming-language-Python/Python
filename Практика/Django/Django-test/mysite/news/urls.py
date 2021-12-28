from django.urls import path, include
# импортировали модуль который работает со списками (ListView)
from django.views.generic import ListView, DetailView
# наш созданный класс
from news.models import Articles
# Если вместо path поставить url и поставить url(r'^contact/$', views.contact, name='contact'), то при написании пути в поисковике contact/wer, будет выдоваться ошибка
urlpatterns = [
    path('', ListView.as_view(queryset = Articles.objects.all().order_by("-date")[:20],
    template_name="news/posts.html")),
    # model - некий наш класс или табличка. template_name - где выводить
    # Либо path('<int:pk>', ...), либо re_path('(?P<pk>\d+)', ...) или вместо re_path написать url
    path('<int:pk>', DetailView.as_view(model = Articles, template_name="news/post.html"))
]