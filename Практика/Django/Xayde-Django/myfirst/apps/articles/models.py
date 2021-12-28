import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
# из чего состоит приложение
# принято называть класс в ед. числе
class Article(models.Model):
    # CharField (хранит небольшое количество символов) - это тип данных (в MySQL это varchar). 1 аргумент - текст, который будет отображаться,
    # 2 аргумент - обязательный длинна вводимого текста
    article_tittle = models.CharField('название статьи', max_length=200)
    # TextField - хранит большое количество символов. Нет обязательных аргументов
    article_text = models.TextField('текст статьи')
    pub_date = models.DateField('дата публикации')
    # используется в Django shell при использовании Article.objects.all()
    def __str__(self):
        return self.article_tittle
    # была ли статья опуликована в последние 7 дней
    # не работает
    def was_published_recently(self):
        return self.pub_date>=( timezone.now() - datetime.timedelta(days=7) )
    # руссификатор
    class Meta:
        verbose_name = 'Статья' # в ед. числе
        verbose_name_plural = 'Статьи' # в мн. числе
class Comment(models.Model):
    # все комментарии привязаны к статьям
    # on_delete=models.CASCADE удаляет комментарии если удалена статья
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    avthor_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)
    def __str__(self):
        return self.avthor_name
    # руссификатор
    class Meta:
        verbose_name = 'Комментарий' # в ед. числе
        verbose_name_plural = 'Комментарии' # в мн. числе