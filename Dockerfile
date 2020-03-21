FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE='opint_framework.conf.settings'
ENV APP_ROOT /usr/src/app
ENV PYTHONPATH ${PYTHONPATH}:${APP_ROOT}
RUN apt-get update && apt-get -y install cron vim python-dev default-libmysqlclient-dev python3-dev
WORKDIR ${APP_ROOT}
ADD requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt