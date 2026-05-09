# TiDB Database Configuration

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),

        'OPTIONS': {
            'charset': 'utf8mb4',
            'autocommit': True,
        },

        'CONN_MAX_AGE': 600,
        'DISABLE_SERVER_SIDE_CURSORS': True,
    }
}

# Production Security Settings

DEBUG = False

ALLOWED_HOSTS = [
    '.onrender.com',
    '127.0.0.1',
    'localhost',
]

CSRF_TRUSTED_ORIGINS = [
    "https://slay-homes.onrender.com",
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')