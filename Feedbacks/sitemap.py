from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class ContactsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return ['contacts', ]

    def location(self, item):
        return reverse(item)
