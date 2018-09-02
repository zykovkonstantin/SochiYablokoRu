from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin
from .models import Investigation, BaseForInvestigation


# Register your models here.
class BaseInvInline(admin.TabularInline, SummernoteInlineModelAdmin):
    model = BaseForInvestigation
    extra = 0
    can_delete = True


class InvAdmin(SummernoteModelAdmin):
    inlines = (BaseInvInline,)
    summernote_fields = ('text',)
    list_display = ['title', 'status']


class BaseInvAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = ['title', 'investigation', 'published_date']
    list_filter = ['investigation', ]


admin.site.register(Investigation, InvAdmin)
admin.site.register(BaseForInvestigation, BaseInvAdmin)
