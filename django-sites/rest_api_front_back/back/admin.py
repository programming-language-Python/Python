from django.contrib import admin

# Register your models here.
from back.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актеры"""
    list_display = ("name", "age")
