from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


class Picture(models.Model):
    picture = models.ImageField(upload_to='pictures', verbose_name='Картинка')
    caption = models.CharField(max_length=50, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='pictures',
                               verbose_name='Автор')
    album = models.ForeignKey('webapp.Album', on_delete=models.PROTECT, blank=True, null=True, related_name='pictures',
                              verbose_name='Альбом')
    private = models.BooleanField(default=False, verbose_name='Приватное')
    favourites = models.ManyToManyField(get_user_model(), related_name='favourites', verbose_name='Избранное')

    def __str__(self):
        return f'{self.id} {self.caption}'

    class Meta:
        db_table = 'pictures'
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Album(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(blank=True, max_length=1000, verbose_name='Описание')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='albums', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.id} {self.name}'

    class Meta:
        db_table = 'albums'
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
