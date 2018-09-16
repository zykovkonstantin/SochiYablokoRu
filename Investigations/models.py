from django.db import models
from django.utils import timezone

status_list = (
    ('1', 'Начало расследования'),
    ('2', 'Сбор информации'),
    ('3', 'Подготовка ответных мер'),
    ('4', 'Ожидание результатов'),
    ('5', 'Анализ полученных результатов'),
    ('6', 'Завершено')
)

basetypes_list = (
    ('1', 'Информация'),
    ('2', 'Жалоба'),
    ('3', 'Запрос'),
    ('4', 'Ответ на жалобу'),
    ('5', 'Ответ на запрос'),
    ('6', 'Итоги')
)


# Create your models here.
class Investigation(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=status_list, default=status_list[0][1])
    published_date = models.DateField(null=True, default=timezone.now)
    description = models.TextField(max_length=250, null=True)
    text = models.TextField(null=True)
    image = models.ImageField(upload_to='investigations/%Y/%m/%d', verbose_name='Изображение', default='default.jpg')

    def get_absolute_url(self):
        return '/project/inv/%i' % self.pk

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рассследование'
        verbose_name_plural = 'Расследования'


class BaseForInvestigation(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT, default='auth.User')
    investigation = models.ForeignKey(Investigation, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=basetypes_list, default=basetypes_list[0][1])
    text = models.TextField()
    published_date = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return '/project/inv/%i/%i' % (self.investigation.pk, self.pk)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Этап расследования'
        verbose_name_plural = 'Этапы расследования'
