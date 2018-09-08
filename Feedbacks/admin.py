from django.contrib import admin
from .models import feedback

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_filter = []
    readonly_fields = ['']