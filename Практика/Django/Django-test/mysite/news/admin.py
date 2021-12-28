from django.contrib import admin
from news.models import Articles
# Register your models here.
# регистрация класса в админку
admin.site.register(Articles)