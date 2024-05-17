FROM --platform=amd64 python:3.11.1-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPYCACHEPREFIX=/tmp/
ENV DOCKER_DEFAULT_PLATFORM=linux/amd64

# Set environment variables for PRODUCTION/DEVELOPMENT
# ENV SYSTEM_ENV=PRODUCTION
ENV DJANGO_SETTINGS_MODULE=api.settings

RUN apt-get update && apt-get -y install \
    libpq-dev gcc make binutils \
    postgresql-client && rm -rf /var/lib/apt/lists/*

# Create unprivileged user to run app as non-root
RUN adduser --disabled-password --gecos '' django
RUN mkdir -p /var/www/staticfiles
RUN chown -R django:django /var/www/staticfiles

# Add user's local bin to the path (i.e. Python site-packages console scripts)
ENV PATH=${PATH}:/home/django/.local/bin

# Add Python requirements
COPY ./requirements.txt /home/django/api/
RUN chown -R django:django /home/django/

USER django
WORKDIR /home/django/api
RUN pip install --no-cache-dir -r requirements.txt

# Copy local code to the container image.
COPY ./ ./

# Run collectstatic, but ignore rest_framework missing files. There
# is a bug – bootstrap lib  CSS code references .map files which are
# not available during collectstatic, but do appear afterwards.
# See: https://github.com/encode/django-rest-framework/issues/4950 &&
# https://stackoverflow.com/a/73411956/14397896
RUN rm -rf /home/django/api/static/
RUN python3 manage.py collectstatic --noinput -i rest_framework

CMD ["./scripts/entrypoint.sh"]
