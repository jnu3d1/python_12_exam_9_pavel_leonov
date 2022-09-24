# Generated by Django 4.1.1 on 2022-09-24 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Время создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
                'db_table': 'albums',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='pictures', verbose_name='Картинка')),
                ('caption', models.CharField(max_length=50, verbose_name='Подпись')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Время создания')),
                ('private', models.BooleanField(default=False, verbose_name='Приватное')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pictures', to='webapp.album', verbose_name='Альбом')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('favourites', models.ManyToManyField(related_name='favourites', to=settings.AUTH_USER_MODEL, verbose_name='Избранное')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
                'db_table': 'pictures',
            },
        ),
    ]
