FROM python:3.9.2-slim
MAINTAINER blinkstu@gmail.com

RUN apt update
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y
COPY requirements.txt requirements.txt
RUN pip3 install gunicorn
RUN pip3 install -r requirements.txt

COPY . /app
WORKDIR /app

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD python manage.py migrate ; python main.py