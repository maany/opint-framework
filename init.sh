#!/bin/bash
export PYTHONPATH=${APP_ROOT}:${PYTHONPATH}
mkdir -p ${APP_ROOT}/migrations/core
mkdir -p ${APP_ROOT}/migrations/data_management
mkdir -p ${APP_ROOT}/migrations/workload_jobsbuster
mkdir -p ${APP_ROOT}/migrations/users
mkdir -p ${APP_ROOT}/migrations/api
touch ${APP_ROOT}/migrations/core/__init__.py
python manage.py makemigrations core data_management workload_jobsbuster users api
python manage.py migrate
python manage.py loaddata initial
echo "0 * * * * root /usr/bin/python3 /code/manage.py rucio_loader_cron >> /code/rucio_loader_output" >> /etc/crontab
service cron start
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '${ADMIN_PASSWORD}')" | python manage.py shell
python3 manage.py runserver 0.0.0.0:8080
