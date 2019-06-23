#!/bin/bash

env=$1
fails=""

inspect() {
  if [ $1 -ne 0 ]; then
    fails="${fails} $2"
  fi
}

dev() {
  docker-compose up -d --build
  docker-compose exec users python manage.py test
  inspect $? users 
  docker-compose exec users pylint --rcfile=.pylintrc --py3k app
}

prod() {
  docker-compose up -d --build
  docker-compose exec users python manage.py create_db
  docker-compose exec users python manage.py test
  docker-compose exec users python manage.py cov
  inspect $? users
  docker-compose exec users pylint --rcfile=.pylintrc --py3k app
}

if [[ "${env}" == "development" ]]; then
  echo "Running app in development mode..."
  dev
elif [[ "${env}" == "production" ]]; then
  echo "Running app in production mode..."
fi

if [ -n "${fails}" ]; then
  echo "Tests failed: ${fails}"
  exit 1
else
  echo "Tests passed!"
  exit 0
fi
