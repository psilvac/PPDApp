#!/bin/bash
# Verificar las dependencias instaladas
cd PPDApp
pip3 list
pip3 install -r requirements.txt
python3 manage.py migrate --noinput
python3 manage.py dbcheck

echo "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin@example.com').exists():
    User.objects.create_superuser(
        email='admin@example.com',
        password='admin123',
        nombre='Admin',
        apellido='User'
    )
" | python manage.py shell


python3 manage.py collectstatic && gunicorn --workers 2 PPDApp.wsgi