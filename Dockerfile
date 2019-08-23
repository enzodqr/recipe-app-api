# Name of the image tag name
FROM python:3.7-alpine
# Name of the maintainer <whatever name we want>
LABEL maintainer="Enzodqr"

# Tells python to run in unbuffered mode (does not allow to buffer the outputs)
ENV PYTHONUNBUFFERED 1

# Create a copy of the requirements.txt file to the Docker image
COPY ./requirements.txt /requirements.txt
# Tells  docker to use the postgres db 
RUN apk add --update --no-cache postgresql-client
# Temporary requierments
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
# Takes the requirements file and installs it into the Docker image
RUN pip install -r /requirements.txt
# Delete Temporary requierments
RUN apk del .tmp-build-deps
# Creates an empty folder on our Docker 
RUN mkdir /app
# Switches to the app directory as the default directory
WORKDIR /app
# Copies from our local machine the app folder to the app folder for the image
COPY ./app /app

# Create a user for running application only call <user>
RUN adduser -D user
# Switches to the user just created
USER user