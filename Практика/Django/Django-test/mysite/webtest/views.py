from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def index(request):
    # вывод
    return HttpResponse("<h3>Привет мир!!!</h3>")


