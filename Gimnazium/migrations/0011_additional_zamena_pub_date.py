# Generated by Django 3.1 on 2021-01-04 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gimnazium', '0010_auto_20201120_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='additional_zamena',
            name='pub_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата публикации'),
        ),
    ]