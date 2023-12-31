# Generated by Django 4.2.4 on 2023-08-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='manga_image')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('year', models.DateTimeField()),
                ('sinopsis', models.TextField()),
                ('genres', models.ManyToManyField(related_name='manga_genre', to='manga.genre')),
            ],
            options={
                'verbose_name': 'manga',
                'verbose_name_plural': 'manga',
            },
        ),
    ]
