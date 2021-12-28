from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=120) 
    body = models.TextField()
    date = models.DateTimeField()
    objects = models.Manager() # для того, чтобы работало Articles.objects.all()
    # вывод заголовки конктерных новосте, вместо объектов
    def __str__(self):
        return self.title
