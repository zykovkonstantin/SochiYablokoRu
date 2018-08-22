from django.db import models
from django.utils import timezone

News_Types = (
    ('НОВОСТИ', 'НОВОСТИ'),
    ('БЛОГ', 'БЛОГ'),
    ('ПУБЛИКАЦИИ', 'ПУБЛИКАЦИИ'),
)


# TODO Расширить модель поста: новость, блог, анонс
class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, default='auth.User',
                               verbose_name='Автор')
    news_type = models.CharField(max_length=20, choices=News_Types, default='НОВОСТИ', verbose_name='Тип публикации')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    # created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    created_date = timezone.now()
    text = models.TextField(verbose_name='Текст публикации')
    published_date = models.DateField(blank=True, null=True, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='%Y/%m/%d', default='default.jpg', verbose_name='Фото на обложку публикации')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Новости и публикации'


class Advertising(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    created_date = timezone.now()
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата мероприятия')
    text = models.TextField(verbose_name='Описание мероприятия')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
