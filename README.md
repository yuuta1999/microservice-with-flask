# Self-taught fullstack

A web application written in microservice design pattern. Using Flask, React, Docker, Nginx.

## Features

>Note: I follow this [tutorial](https://docs.docker.com/get-started/) for Docker.

- [***Docker***](https://www.docker.com/): Full Docker integration. Every services run in Docker-based.

- [***Docker Compose***](https://docs.docker.com/compose/): Define and run multi-container Docker application. Use docker-compose for only local developing.

- [***Docker Swarm***](https://docs.docker.com/engine/swarm/): Deploy application.

- [***Nginx***](https://www.nginx.com/): Hide all backend servers from naughty clients.

- [***Heroku***](https://www.heroku.com/): Cloud service. Easy to use for personal project.

- [***Gunicorn***](https://gunicorn.org/): Provide WSGI HTTP server. (Recommended when using Nginx for Flask application).

- Full Python backend, using [***Flask***](http://flask.pocoo.org/) and:
  
  - [**Flask-SQLAlchemy**](https://flask-sqlalchemy.palletsprojects.com/en/2.x/): Add supports for SQLAlchemy to this application.

  - [**Psycopg2-binary**](http://initd.org/psycopg/docs/install.html): Use PostgreSQL in this application.

  - [**Marshmallow**](https://github.com/marshmallow-code/marshmallow): Convert some complex objects to Python native datatypes.

  - [**Flask-Bcrypt**](https://flask-bcrypt.readthedocs.io/en/latest/): Secure authentication with hashed password with Bcrypt.

  - [**Flask-JWT-Extended**](https://flask-jwt-extended.readthedocs.io/en/latest/): Use JSON Web Token (JWT) to authenticate users login.

  - [**Flask-Migrate**](https://flask-migrate.readthedocs.io/en/latest/): Handle SQLAlchemy database migration for FLask.

  - [**Flask-CORS**](https://flask-cors.readthedocs.io/en/latest/): Handle Cross Origin Resource Sharing (CORS), make AJAX call possible.
  