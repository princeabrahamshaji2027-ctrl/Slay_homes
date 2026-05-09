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
            'ssl': {
                'ca': env('SSL_CA', default='/etc/ssl/cert.pem')
            },
            'connect_timeout': 60,
            'read_timeout': 60,
            'write_timeout': 60,
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