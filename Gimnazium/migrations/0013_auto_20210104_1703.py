# Generated by Django 3.1 on 2021-01-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gimnazium', '0012_auto_20210104_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additional_zamena',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата публикации'),
        ),
    ]
