# Generated by Django 3.1 on 2020-11-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gimnazium', '0009_auto_20201112_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additional_zamena',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterField(
            model_name='additional_zamena',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Описание новости'),
        ),
        migrations.AlterField(
            model_name='additional_zamena',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название новости'),
        ),
    ]
