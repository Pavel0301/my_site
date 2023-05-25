# ***Настройка Установленных Библиотек***

## **INSTALL_APP**

```commandline
#settings

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
     'django.contrib.sites',
    'django.contrib.staticfiles',
     "debug_toolbar",
      #'channels',
    # https://docs.djangoproject.com/en/4.0/ref/contrib/humanize/
    'django.contrib.humanize',
    
     # pascages install
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    
    
    
   
    'crispy_forms',
    'ckeditor',
    
   

    # мои приложения
    'blog.apps.BlogConfig',  # когда применяете сигналы, метки
    
    
    # должна быть последней
    # https://github.com/un1t/django-cleanup
    'django_cleanup.apps.CleanupConfig',

]

```



## **Static and Media**

```commandline
#settings.py


# https://docs.djangoproject.com/en/4.0/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


STATICFILES_DIRS = [
    
    #os.path.join(BASE_DIR, "my_site/templates"),
   
]


STATICFILES_FINDERS = [

    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
   ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'
```

```commandline
#urls.py

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## **Templates**

```commandline
#settings.py


.....................



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


```

## **django-crispy-forms**

[django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)


```commandline
INSTALLED_APPS+

and 

..................................


CRISPY_TEMPLATE_PACK = 'uni_form'




```


## **django-ckeditor**

[django-ckeditor](https://pypi.org/project/django-ckeditor/)

```commandline
#settings.py




INSTALLED_APPS = [

    ..........

    'ckeditor',
 ] 




  

# django-ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'width':'auto',
    },
}

# End django-ckeditor
```

## **django-allauth**

[django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

```commandline

# settings.py



INSTALLED_APPS = [

      .............

    'django.contrib.sites',
    'django.contrib.staticfiles',
    
     # pascages install
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    
    
    
   
    ......................

]

SITE_ID = 1




# django-allauth
# https://django-allauth.readthedocs.io/en/latest/installation.html

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}


# End django-allauth
```

```commandline
#urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #path('register/', user_views.register, name='register'),
    #path('profile/', user_views.profile, name='profile'),
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    #path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    #path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    #path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    
    
    path('accounts/', include('allauth.urls')),
    
    
]
```

## **django.contrib.humanize**

[django.contrib.humanize](https://docs.djangoproject.com/en/4.2/ref/contrib/humanize/)

```commandline

INSTALLED_APPS = [

    ...............

    'django.contrib.staticfiles',
    # https://docs.djangoproject.com/en/4.0/ref/contrib/humanize/
    'django.contrib.humanize',

    ......
]
```

## **django-debug-toolbar**

[django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

```commandline
#settings



# django-debug-toolbar
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]




INSTALLED_APPS = [

    .................

    'django.contrib.staticfiles',
     "debug_toolbar",
    ....................
]



MIDDLEWARE = [

    ............

    "debug_toolbar.middleware.DebugToolbarMiddleware", # django-debug-toolbar
]
```

```commandline

#urls.py

if settings.DEBUG:
       
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
```




















## **Настройка dotenv**

[dotenv](https://pypi.org/project/python-dotenv/)

`pip install python-dotenv`

```python


from pathlib import Path
import os
from dotenv import load_dotenv
from django.contrib.messages import constants as messages

# Loading ENV
env_path = Path('.') / '.env'

#env_path = '.test.env'
load_dotenv(dotenv_path=env_path)
```

## **Channels**

```commandline

# settings.py




INSTALLED_APPS = [

     ..................
     
     'django.contrib.sites',
    'django.contrib.staticfiles',
     "debug_toolbar",
      #'channels',

     ................

]


# django-channels
"""
ASGI_APPLICATION = "practice_django.routing.application"

CHANNEL_LAYERS = {
    "default":{
        "BACKEND":"channels.layers.InMemoryChannelLayer"
    },
}
"""

# End django-channels
```


## **All Settings file**

```commandline

# 


# весь settings





# -*- coding: utf-8 -*-

# django-debug-toolbar
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
"""
Django settings for practice_django project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""


import os
from pathlib import Path
from django.contrib.messages import constants as messages

# python-dotenv
# https://pypi.org/project/python-dotenv/
# .env в корне проекта

from dotenv import load_dotenv
# Loading ENV

env_path = Path('.') / '.env'

#env_path = '.test.env'
load_dotenv(dotenv_path=env_path)

# End python-dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-3_zy&z)7k&+fgw3yq#97&&4d3d(ii^(bcg6)yl7uz_(^bct45k'

SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# разрешённые хосты
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
     'django.contrib.sites',
    'django.contrib.staticfiles',
     "debug_toolbar",
      #'channels',
    # https://docs.djangoproject.com/en/4.0/ref/contrib/humanize/
    'django.contrib.humanize',
    
     # pascages install
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    
    
    
   
    'crispy_forms',
    'ckeditor',
    
   

    # мои приложения
    'blog.apps.BlogConfig',  # когда применяете сигналы, метки
    
    
    # должна быть последней
    # https://github.com/un1t/django-cleanup
    'django_cleanup.apps.CleanupConfig',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware", # django-debug-toolbar
]

ROOT_URLCONF = 'practice_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),

                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# django-allauth
# https://django-allauth.readthedocs.io/en/latest/installation.html

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}


# End django-allauth


WSGI_APPLICATION = 'practice_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_practice_django_1.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# https://docs.djangoproject.com/en/4.0/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


STATICFILES_DIRS = [

    #os.path.join(BASE_DIR, "my_site/templates"),

]


STATICFILES_FINDERS = [

    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django-crispy-forms
# https://django-crispy-forms.readthedocs.io/en/latest/install.html

# CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'uni_form'

# End django-crispy-forms


# django-ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'width':'auto',
    },
}

# End django-ckeditor


# django-channels
"""
ASGI_APPLICATION = "practice_django.routing.application"

CHANNEL_LAYERS = {
    "default":{
        "BACKEND":"channels.layers.InMemoryChannelLayer"
    },
}
"""

# End django-channels


# email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_USER')     
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASS') 

# End Email

GOOGLE_RECAPTCHA_SECRET_KEY = os.getenv("GOOGLE_RECAPTCHA_SECRET_KEY")

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
}
```

```commandline

#





# .env


SECRET_KEY=django-insecure-3_zy&z)7k&+fgw4569q#97&&4d3d(ii^(bcg6)yl7uz_(^bct45k
GOOGLE_RECAPTCHA_SECRET_KEY=6LdVwogdAAAAA47894GKxqjEnHd7u5z-_tq91n
DEBUG=True
EMAIL_USER=xxxx@mail.ru
EMAIL_PASS=xxxxxxxxx
EMAIL_PORT=587

```