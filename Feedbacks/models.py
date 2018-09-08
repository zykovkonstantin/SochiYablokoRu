from django.db import models
from django.utils import timezone

type_list = (
    ('1', 'Сообщение об ошибке'),
    ('2', 'Призыв о помощи'),
    ('3', 'Полезная информация'),
    ('4', 'Другое')
)


class feedback(models.Model):
    feedback_type = models.CharField(max_length=50, choices=type_list, help_text='Тип обращения')
    author_name = models.CharField(max_length=100, help_text='Ваше имя')
    author_email = models.EmailField(help_text='Ваш адрес электронной почты')
    title = models.CharField(max_length=100, help_text='Тема обращения')
    text = models.TextField(help_text='Текст обращения')
    created_date = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.title
