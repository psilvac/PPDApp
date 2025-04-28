#!/bin/bash
# Verificar las dependencias instaladas
cd PPDApp
pip3 list
pip3 install -r requirements.txt
python3 manage.py migrate --noinput
python3 manage.py showmigrations || echo "❌ Error de conexión a la base de datos"
python3 manage.py migrate --fake auth
python3 manage.py migrate


echo "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(email='admin@example.com').exists():
    User.objects.create_superuser(
        email='admin@example.com',
        password='admin',
        nombre='Jorge',
        apellido='Sanmartin'
    )
" | python3 manage.py shell

echo "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(email='admin@admin.com').exists():
    User.objects.create_superuser(
        email='admin@admin.com',
        password='admin123admin',
        nombre='Pablo',
        apellido='Silva'
    )
" | python3 manage.py shell



echo "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(email='administrado@admin.com').exists():
    User.objects.create_superuser(
        email='administrado@admin.com',
        password='admin',
        nombre='Jorge',
        apellido='Sanmartin'
    )
" | python3 manage.py shell

python3 manage.py collectstatic && gunicorn --workers 2 PPDApp.wsgi
