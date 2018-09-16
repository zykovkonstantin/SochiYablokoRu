"""SochiYablokoRu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import urls
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from YablokoNews.views import index, news, news_add, news_detail, adv_detail, privacy_policy
from YablokoNews.sitemap import NewsSitemap, AdvSitemap
from Investigations.views import investigations, investigations_detail, base_inv_detail
from Investigations.sitemap import InvSitemap, BaseInvSitemap
from Feedbacks.views import contacts
from Feedbacks.sitemap import ContactsSitemap
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'news': NewsSitemap(),
    'adv': AdvSitemap(),
    'contscts': ContactsSitemap(),
    'inv': InvSitemap(),
    'baseinv': BaseInvSitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(urls)),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<str:type>/', news, name='news'),
    path('news/add/', news_add, name='news_add'),
    path('news/<int:pk>', news_detail, name='news_detail'),
    path('adv/<int:pk>', adv_detail, name='adv_detail'),
    path('projects/inv/', investigations, name='projects'),
    path('projects/inv/<int:pk>', investigations_detail, name='inv_detail'),
    path('projects/inv/<int:inv_pk>/<int:base_pk>', base_inv_detail, name='base_inv_detail'),
    path('summernote/', include('django_summernote.urls')),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
