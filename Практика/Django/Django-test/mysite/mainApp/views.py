# позволяет выводить большие куски сайта или даже весь сайт
from django.shortcuts import render
# Create your views here.
def index(request):
    # 1 обязательный параметр request,
    # 2 путь к файлу, который хотим вывести,
    # 3 словарь это будет набор переменнных, данных, которые будут применяться в homePage.html
    return render(request, 'mainApp/homePage.html')
def contact(request):
    return render(request, 'mainApp/basic.html', {'values':['Если у вас остались вопросы, то задавайте их мне по телефону', '(151) 056-69-69']})