from django import forms
from .models import News, Advertising
from django_summernote.widgets import SummernoteWidget


class NewsForm(forms.ModelForm):
    text = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = News
        fields = ('title', 'text', 'image', 'published_date')


class AdvForm(forms.ModelForm):
    text = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Advertising
        fields = ('title', 'text', 'published_date')
