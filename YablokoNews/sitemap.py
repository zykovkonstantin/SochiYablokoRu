from django.contrib.sitemaps import Sitemap
from .models import News, Advertising


class NewsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return News.objects.all()


class AdvSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Advertising.objects.all()
