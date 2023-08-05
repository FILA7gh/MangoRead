# Generated by Django 4.2.4 on 2023-08-05 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(blank=True, max_length=255)),
                ('link_one', models.URLField(blank=True)),
                ('link_two', models.URLField(blank=True)),
                ('link_three', models.URLField(blank=True)),
                ('map', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'about us',
            },
        ),
    ]
