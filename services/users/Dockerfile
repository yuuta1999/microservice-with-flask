FROM python:3.7-slim

# install some stuff
RUN apt-get update && \
    apt-get clean

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . /usr/src/app

# run server
ENTRYPOINT [ "sh", "/usr/src/app/entrypoint.sh" ]

