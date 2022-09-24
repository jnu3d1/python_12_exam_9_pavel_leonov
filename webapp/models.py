from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Picture(models.Model):
    picture = models.ImageField(upload_to='pictures', verbose_name='Картинка')
    caption = models.CharField(max_length=50, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    author = models.ForeignKey(get_user_model(), default=1)