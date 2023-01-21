#!/usr/bin/env bash
# exit on error
set -o errexit
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin',
'admin@example.com', 'password')" | python manage.py shell
