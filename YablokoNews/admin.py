from django.contrib import admin
from .models import News, Advertising
from django_summernote.admin import SummernoteModelAdmin


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


# Register your models here.
admin.site.register(News, SomeModelAdmin)

admin.site.register(Advertising, SomeModelAdmin)

