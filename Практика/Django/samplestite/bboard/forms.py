from django.forms import ModelForm
from .models import Bd
# создали файл forms.py для принятия формы. Нужно для страницы, где мы будем создавать новые объявления
'''
В классе формы мы объявили вложенный класс Meta, в котором
указали параметры нашей формы: класс модели, с которой она связана (атрибут
класса model), и последовательность из имен полей модели, которые должны
присутствовать в форме (атрибут класса fields).
'''
class BdForm (ModelForm):
    class Meta:
        model = Bd
        fields = ('title', 'content', 'price', 'rubric')

