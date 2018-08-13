from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import News


# Create your views here.
def index(request):
    last_news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
    return render(request, 'main_page.html', {'last_news': last_news})


def news(request):
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news.html', {'news': news})


def news_detail(request, pk):
    new = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'new': new})
