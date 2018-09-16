from django.db import models
from django.utils import timezone
from SochiYablokoRu.settings import MEDIA_URL
from UserProfiles.models import UserProfile

News_Types = (
    ('НОВОСТИ', 'НОВОСТИ'),
    ('БЛОГ', 'БЛОГ'),
    ('ПУБЛИКАЦИИ', 'ПУБЛИКАЦИИ'),
)


# TODO Расширить модель поста: новость, блог, анонс
class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, verbose_name='Автор',
                               default='auth.User')
    news_type = models.CharField(max_length=20, choices=News_Types, default='НОВОСТИ', verbose_name='Тип публикации')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    # created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    created_date = timezone.now()
    text = models.TextField(verbose_name='Текст публикации')
    published_date = models.DateField(blank=True, null=True, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='news/%Y/%m/%d', default='default.jpg',
                              verbose_name='Фото на обложку публикации')

    def author_name(self):
        return ('%s' + ' ' + '%s') % (self.author.first_name, self.author.last_name)

    def author_img(self):
        image = UserProfile.objects.filter(user_id=self.author.id).values_list('avatar', flat=True)
        return '%s%s' % (MEDIA_URL, image[0])

    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe('<img src="%s" width="100"/>' % self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Обложка'
    image_img.allow_tags = True

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return "/news/%i" % self.pk

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

    def get_absolute_url(self):
        return "/adv/%i" % self.pk

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
