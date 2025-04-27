from .settings import *  # Importa la configuración base

# Usar una base de datos en memoria para pruebas
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Usualmente en AWS usarás PostgreSQL
        'NAME': "testdb",           # El nombre de tu base de datos
        'USER': "postgres",           # El usuario
        'PASSWORD': '1234',   # La contraseña
        'HOST': 'localhost',           # El host de la base de datos
        'PORT': '5432',   # El puerto, 5432 por defecto
    }
}
TESTING = True
# Desactivar contraseñas complejas en pruebas
#AUTH_PASSWORD_VALIDATORS = []

# Configuraciones adicionales para optimizar las pruebas
#DEBUG = False
#SECRET_KEY = "test_secret_key"
#EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"  # Usa un backend de correo en memoria
#PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]  # Acelera el hashing de contraseñas en pruebas