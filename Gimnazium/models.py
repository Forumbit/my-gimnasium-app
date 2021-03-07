from django.db import models
import time
from django.utils import timezone
import datetime
a = []
for i in range(5, 12):
    j = (f'{i}', f'{i}')
    a.append(j)

b = [
    ('А', 'А'),
    ('Б', 'Б'),
    ('А и Б', 'А и Б')
]

c = [
    ('Английский', 'Английский'),
    ('Астрономия', 'Астрономия'),
    ('Биология', 'Биология'),
    ('Индивидуальный проект', 'Индивидуальный проект'),
    ('Информатика и ИКТ', 'Информатика и ИКТ'),
    ('История', 'История'),
    ('Литература', 'Литература'),
    ('Математика', 'Математика'),
    ('Обществознание', 'Обществознание'),
    ('ОБЖ', 'ОБЖ'),
    ('Право', 'Право'),
    ('Родная (татарская) литература', 'Родная (татарская) литература'),
    ('Родной (татарский) язык', 'Родной (татарский) язык'),
    ('Русский язык', 'Русский язык'),
    ('Физика', 'Физика'),
    ('Физическая культура', 'Физическая культура'),
    ('Химия', 'Химия'),
]


# Create your models here.
class Zamena(models.Model):
    how_lesson = models.IntegerField(verbose_name='Урок', null=True)
    lesson = models.CharField(max_length=2, choices=a, default=a[0], verbose_name='Класс')
    letter = models.CharField(max_length=5, choices=b, default=b[0], verbose_name='Буква')
    predmet = models.CharField(max_length=100, choices=c, default=c[0], verbose_name='Предмет')
    cabinet = models.IntegerField(verbose_name='Кабинет', null=True)

    def __str__(self):
        return f'Класс: {self.lesson}{self.letter}, замена {self.predmet}, кабинет {self.cabinet}'


class Additional_zamena(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название новости')
    description = models.TextField(verbose_name='Описание новости')
    pub_date = models.TimeField(verbose_name="Дата публикации", auto_now_add = True, blank = True, null = True)


    class Meta:
        ordering = ["-pk"]
