from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import News, Advertising


# Create your views here.
def index(request):
    last_news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
    advertisings = Advertising.objects.filter(published_date__gte=timezone.now()).order_by('published_date')
    return render(request, 'main_page.html', {'last_news': last_news, 'advertisings': advertisings})


# TODO после расширения модели, нужны выборки по типу поста
def news(request):
    news = News.objects.filter(published_date__lte=timezone.now(), news_type='НОВОСТИ').order_by('published_date')
    return render(request, 'news.html', {'news': news})


def news_detail(request, pk):
    one_news = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'one_news': one_news})


def adv_detail(request, pk):
    adv = get_object_or_404(Advertising, pk=pk)
    return render(request, 'news_detail.html', {'adv': adv})
