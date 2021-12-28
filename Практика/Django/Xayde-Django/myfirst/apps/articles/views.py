from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Comment
# Create your views here.
def index (request):
    # return HttpResponse("Привет мир!!!")
    #return render (request, 'articles/list.html')
    # order_by сортировка знак '-' обозначает, что сортирует в обратном порядке
    latest_articles_list = Article.objects.order_by('-pub_date')[:5] # последние 5 статьей вернёт
    # 3 аргумент это контекст
    return render (request, 'articles/list.html', {'latest_articles_list': latest_articles_list})