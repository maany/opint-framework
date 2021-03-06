[![Build Status](https://travis-ci.com/operationalintelligence/rucio-opint-backend.svg?branch=master)](https://travis-ci.com/operationalintelligence/rucio-opint-backend)

## Description

OpInt Framework.

## Installation

Fork the repo into your personal project and clone the project.
```commandline
cd ~/projects/opint-framework/
git clone https://github.com/operationalintelligence/opint-framework
```

Create a new python3 virtual environment and activate it:
```commandline
virtualenv -p python3 ~/environments/opint-framework
source ~/environments/opint-framework/bin/activate
```


Install Python dependencies:
```commandline
cd ~/projects/opint-framework/opint-framework
pip install -r requirements.txt
``` 

Export settings module:
```commandline
export DJANGO_SETTINGS_MODULE='opint_framework.conf.settings'
```

The following environmental variables can be set:
```commandline
API_KEY: The key for Monit Grafana's API
DB_PASS: The pass for the produciton database.
For Development you can enable sqlite populating the MODE env variable:
export MODE=dev 
```
Create DB:
```commandline
python manage.py makemigrations core data_management workload_jobsbuster users api
python manage.py migrate
```

Populate DB with initial data: (Currently deprecated. Data should be ported to the new models.)
```commandline
python manage.py loaddata initial
```

## Running the app:
Navigate to the project's directory:
```commandline
cd ~/projects/opint-framework
```
Run the django server:
```commandline
python manage.py runserver
```

## Fetching information: (Currently deprecated. To be ported to new Scheduler paradigm)
In order to fetch issues from HDFS:
```commandline
python manage.py hdfs_loader_cron
```
For a specific date:
```commandline
python manage.py hdfs_loader_cron --date=12/1/2019
```

In order to fetch issues from Monit-Grafana ES API:
```commandline
python manage.py rucio_loader_cron
```
