from django.contrib import admin
from .models import News, Advertising
from django_summernote.admin import SummernoteModelAdmin


class NewsModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('text',)
    list_display = ('news_type', 'title', 'published_date', 'author', 'image', 'image_img')
    list_filter = ['news_type', 'author']
    readonly_fields = ['image_img', ]
    fields = ['author', 'news_type', 'title', 'text', 'published_date', 'image', 'image_img']


class AdvModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = ('published_date', 'title')


# Register your models here.
admin.site.register(News, NewsModelAdmin)

admin.site.register(Advertising, AdvModelAdmin)
