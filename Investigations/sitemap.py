from django.contrib.sitemaps import Sitemap
from .models import Investigation, BaseForInvestigation


class InvSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Investigation.objects.all()


class BaseInvSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return BaseForInvestigation.objects.all()
