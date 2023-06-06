


"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),

    path('my_site/', include('blog.urls'), name='blog_urls'),
    path('my_site/', include('discussions.urls'), name='discussions_urls'),
    path('my_site/', include('forms_app.urls'), name='forms_app_urls'),
    path('accounts/', include('allauth.urls')),
    path('profile/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('messages/', include('messenger.urls'), name='messenger_urls'),

]
    #path('__debug__/', include('debug_toolbar.urls')),


    #https://django-allauth.readthedocs.io/en/latest/installation.html
    #path('accounts/', include('allauth.urls')),

    # https://pypi.org/project/django-ckeditor/#installation
    #path('ckeditor/', include('ckeditor_uploader.urls')),





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)