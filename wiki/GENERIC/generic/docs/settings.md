Настройка статики и медиа 

[media and static](https://docs.djangoproject.com/en/4.2/ref/settings/#media-url)
```commandline
STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "my_site/templates")
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppStaticFilesFinder',
]

MEDIA_URL = "media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```