#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Esperando pelo servico do postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL iniciado"
fi

chown -R $GID:$UID /usr/src/app
chmod -R 777 /usr/src/app

cp -r ./bank_django_nuxt3_api/.env.dev.example ./bank_django_nuxt3_api/.env
python manage.py migrate
python manage.py initadmin
python manage.py runserver 0.0.0.0:8000

exec "$@"