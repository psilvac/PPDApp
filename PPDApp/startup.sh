#!/bin/bash
# Verificar las dependencias instaladas
cd PPDApp
pip3 list
pip3 install -r requirements.txt
python3 manage.py migrate --noinput
python3 manage.py dbcheck
python3 manage.py createsuperuser --noinput --nombre Jorge --apellido sanmartin
python3 manage.py collectstatic && gunicorn --workers 2 PPDApp.wsgi