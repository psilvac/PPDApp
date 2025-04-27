from .settings import *
import os

ALLOWED_HOSTS = ["*",]

CSRF_TRUSTED_ORIGINS = [
    "*",
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'test_db'),        # Nombre de la base que se levanta
        'USER': os.getenv('DB_USER', 'postgres'),       # Usuario que se define en el servicio
        'PASSWORD': os.getenv('DB_PASSWORD', 'postgres'), # Contraseña
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),       # Host local
        'PORT': os.getenv('DB_PORT', '5432'),            # Puerto
    }
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]