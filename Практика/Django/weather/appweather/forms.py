from .models import City
# ModelForm - форма будет содержать теже самые поля, которые есть в самой таблицы
# TextInput - позволяет добавлять атрибуты к полям в форме
from django.forms import ModelForm, TextInput
class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name':TextInput(attrs={
        'class':'form-control',
        'name':'city',
        'id':'city',
        'placeholder':'Введите город'
        })}
