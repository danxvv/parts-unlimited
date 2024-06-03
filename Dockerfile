FROM python:3.11-alpine3.20

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN chmod +x /usr/src/app/entrypoint.sh


ENTRYPOINT ["/bin/sh", "/usr/src/app/entrypoint.sh"]
