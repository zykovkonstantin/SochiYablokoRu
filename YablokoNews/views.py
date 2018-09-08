from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger
from django.utils import timezone
from .models import News, Advertising
from .forms import NewsForm


# Create your views here.
def index(request):
    last_news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
    advertisings = Advertising.objects.filter(published_date__gte=timezone.now()).order_by('published_date')
    return render(request, 'main_page.html', {'last_news': last_news, 'advertisings': advertisings})


def news(request, type):
    if type == 'news':
        all_news_list = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    elif type == 'blog':
        all_news_list = News.objects.filter(published_date__lte=timezone.now(), news_type='БЛОГ').order_by(
            '-published_date')
    elif type == 'publications':
        all_news_list = News.objects.filter(published_date__lte=timezone.now(), news_type='ПУБЛИКАЦИЯ').order_by(
            '-published_date')
    paginator = Paginator(object_list=all_news_list, per_page=20, orphans=3)
    page = request.GET.get('page')
    try:
        all_news = paginator.page(page)
    except PageNotAnInteger:
        all_news = paginator.page(1)
    return render(request, 'news/news.html', {'all_news': all_news})


# @login_required
def news_add(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        post = form.save(commit=False)
        post.author = request.user
        post.created_date = timezone.now()
        post.save()
        return redirect('news_detail', pk=post.pk)
    else:
        form = NewsForm()
    return render(request, 'news/news_add.html', {'form': form})


def news_detail(request, pk):
    one_news = get_object_or_404(News, pk=pk)
    last_news = News.objects.filter(published_date__lte=timezone.now()).exclude(pk=pk).order_by('-published_date')[:10]
    return render(request, 'news/news_detail.html', {'one_news': one_news, 'last_news': last_news})


def adv_detail(request, pk):
    adv = get_object_or_404(Advertising, pk=pk)
    last_news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:10]
    return render(request, 'news/news_detail.html', {'one_news': adv, 'last_news': last_news})


def privacy_policy(request):
    return render(request, 'privacy_policy.html')
