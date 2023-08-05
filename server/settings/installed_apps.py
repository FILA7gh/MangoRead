PROJECT_APPS = [
    'server.apps.manga',
    'server.apps.user',
    'server.apps.about_us',
    'server.apps.reviews',
]

OTHER_APPS = [
    'jazzmin',
    'drf_yasg',
    'rest_framework_simplejwt',
    'rest_framework',
    'avatar',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = [
    *OTHER_APPS,
    *DJANGO_APPS,
    *PROJECT_APPS
]
