from django.apps import AppConfig
from django_summernote.apps import DjangoSummernoteConfig


class YablokonewsConfig(AppConfig):
    name = 'YablokoNews'
    verbose_name = 'Сайт Яблоко в Сочи'


DjangoSummernoteConfig.verbose_name = 'Фотографии'
