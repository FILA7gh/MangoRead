# Generated by Django 4.2.4 on 2023-08-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='year',
            field=models.DateField(),
        ),
    ]
