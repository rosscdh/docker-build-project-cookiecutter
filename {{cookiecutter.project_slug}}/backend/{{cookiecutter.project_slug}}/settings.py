"""
"""
import os
import raven

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^-od5@t_^h8e#furs$w=*tmbgarr#p0t%ww%%^3hf947jr=ms$'

# SECURITY WARNING: don't run with debug turned on in production!
TRUTHY = (True, 'True', 'true', 't', 1, '1')
DEBUG = os.getenv('DEBUG') in TRUTHY

ALLOWED_HOSTS = ['*']


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

APP_APPS = [
    'ef.apps.public',
    'ef.apps.video',
    'ef.apps.categories',
]

HELPER_APPS = [
    'django_extensions',
    'corsheaders',
    'rest_framework',

    'crispy_forms',

    'storages',
    'pipeline',

    # 'django_rq',
    'spurl',
    'raven.contrib.django.raven_compat',

    'health_check',                             # required
    'health_check.db',                          # stock Django health checkers
    'health_check.cache',
]

INSTALLED_APPS = DJANGO_APPS + APP_APPS + HELPER_APPS

#
# defaults
#
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
USE_ETAGS = os.getenv('USE_ETAGS', False) in TRUTHY

if DEBUG is True:
    #
    # Development
    #
    INSTALLED_APPS += [
        'django_seed',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
else:
    #
    # PROD
    #
    # ONLY if its specifically set to production
    if os.getenv('DJANGO_ENV', 'development') == 'production':
        if os.getenv('EMAIL_HOST'):
            EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            EMAIL_HOST = os.getenv('EMAIL_HOST')
            EMAIL_PORT = os.getenv('EMAIL_PORT')
            EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
            EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
            #EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
            #EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL')
            #EMAIL_TIMEOUT = os.getenv('EMAIL_TIMEOUT')

    USE_ETAGS = os.getenv('USE_ETAGS', True) in TRUTHY

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.gzip.GZipMiddleware',
        'pipeline.middleware.MinifyHTMLMiddleware',
    ]


ROOT_URLCONF = 'ef.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'ef', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ef.apps.public.context_processors.ziggeo',
            ],
        },
    },
]
#
# Cached template loaders
#
if DEBUG is False:
    # in production make templates load fast
    del(TEMPLATES[0]['APP_DIRS'])
    TEMPLATES[0]['OPTIONS']['loaders'] = [
        ('django.template.loaders.cached.Loader', [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]),
    ]


WSGI_APPLICATION = 'ef.wsgi.application'

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": os.getenv('REDIS_LOCATION', 'redis://redis:6379/0'),
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }


SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
        #'OPTIONS': {'sslmode': 'require'},
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/s/'
MEDIA_URL = '/m/'

STATIC_ROOT = os.getenv('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))
MEDIA_ROOT = os.getenv('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))


CORS_ORIGIN_WHITELIST = (
    '*',
)

CRISPY_TEMPLATE_PACK = 'bootstrap'

RQ_QUEUES = {
    'default': {
        'HOST': os.getenv('REDIS_HOST', 'redis'),
        'PORT': os.getenv('REDIS_PORT', '6379'),
        'DB': os.getenv('REDIS_DB', '1'),
        #'PASSWORD': 'some-password',
        'DEFAULT_TIMEOUT': 360,
    },
    'high': {
        'HOST': os.getenv('REDIS_HOST', 'redis'),
        'PORT': os.getenv('REDIS_PORT', '6379'),
        'DB': os.getenv('REDIS_DB', '1'),
        #'PASSWORD': 'some-password',
        'DEFAULT_TIMEOUT': 360,
    }
}

ZIGGEO_TOKEN = os.getenv('ZIGGEO_TOKEN')
ZIGGEO_PRIVATE_KEY = os.getenv('ZIGGEO_PRIVATE_KEY')
ZIGGEO_ENCRYPTIONKEY = os.getenv('ZIGGEO_ENCRYPTIONKEY')

PIPELINE = {
    'PIPELINE_ENABLED': True,
    # 'CSS_COMPRESSOR': 'pipeline.compressors.yuglify.YuglifyCompressor',
    # 'JS_COMPRESSOR': 'pipeline.compressors.uglifyjs.UglifyJSCompressor',
    # 'UGLIFYJS_BINARY': '/usr/local/bin/uglify',
    # 'COMPILERS': ('pipeline.compilers.sass.SASSCompiler',),
    'STYLESHEETS': {
    },
    'JAVASCRIPT': {
    }
}

# HAYSTACK_CONNECTIONS = {
#     # 'default': {
#     #     'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#     #     'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
#     # },
#     'default': {
#         'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#         'URL': os.getenv('HAYSTACK_ES_URL', 'http://elasticsearch:9200/'),
#         #'URL': 'http://localhost:9200/',
#         'INDEX_NAME': 'ef',
#     },
# }
#
# Cant use this due to model postsave dependency. Maybe switch to using the meta as the observed model?
#
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

RAVEN_CONFIG = {
    'dsn': 'https://:@sentry.io/',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    #'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}