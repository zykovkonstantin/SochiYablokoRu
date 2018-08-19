from django.db import models
from django.utils import timezone

News_Types = (
    ('НОВОСТИ', 'НОВОСТИ'),
    ('БЛОГ', 'БЛОГ'),
    ('ПУБЛИКАЦИИ', 'ПУБЛИКАЦИИ'),
)


# TODO Расширить модель поста: новость, блог, анонс
class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    news_type = models.CharField(max_length=20, choices=News_Types, default='НОВОСТИ')
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='%Y/%m/%d', default='default.jpg')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Новости и публикации'


class Advertising(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
