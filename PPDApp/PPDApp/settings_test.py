from .settings import *  # Importa la configuración base

# Usar una base de datos en memoria para tests
DATABASES = {
    "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",  # Usa una base de datos en memoria (rápida)
        }
}
TESTING = True
# Desactivar contraseñas complejas en tests
#AUTH_PASSWORD_VALIDATORS = []
