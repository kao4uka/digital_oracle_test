#!/bin/bash

cd .
python manage.py migrate
python manage.py runserver
