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
from django.urls import path, include
from YablokoNews import views as news_views
from Investigations import views as inv_views
from Feedbacks import views as fdb_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(urls)),
    path('', news_views.index, name='index'),
    path('contacts/', fdb_views.contacts, name='contacts'),
    path('<str:type>/', news_views.news, name='news'),
    path('news/add/', news_views.news_add, name='news_add'),
    path('news/<int:pk>', news_views.news_detail, name='news_detail'),
    path('adv/<int:pk>', news_views.adv_detail, name='adv_detail'),
    path('projects/inv/', inv_views.investigations, name='projects'),
    path('projects/inv/<int:pk>', inv_views.investigations_detail, name='inv_detail'),
    path('projects/inv/<int:inv_pk>/<int:base_pk>', inv_views.base_inv_detail, name='base_inv_detail'),
    path('summernote/', include('django_summernote.urls')),
    path('privacy_policy/', news_views.privacy_policy, name='privacy_policy')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
