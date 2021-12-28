from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=30)
    objects = models.Manager() # для того, чтобы работало Articles.objects.all()
    def __str__(self):
        return self.name