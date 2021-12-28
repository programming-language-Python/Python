from django.contrib import admin

# Register your models here.
from .models import Bd
# объявили класс-редактор
class BdAdmin(admin.ModelAdmin):
# list_display - последовательность имен полей, которые должны выводиться в списке записей;
# list_display_links - последовательность имен полей, которые должны быть преобразованы в гиперссылки, ведущие на страницу правки записи;
# search_fields - последовательность имен полей, по которым должна вьполняться фильтрация (поиск).
    list_display = ('title', 'content', 'price', 'published','rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)
admin.site.register(Bd,BdAdmin)
from .models import Rubric
admin.site.register(Rubric)