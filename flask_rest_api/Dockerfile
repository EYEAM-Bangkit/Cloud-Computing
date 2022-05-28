FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /
WORKDIR $APP_HOME
COPY . ./

RUN pip install -r requirements.txt
EXPOSE 4000
CMD gunicorn -b 0.0.0.0:4000 --workers 1 --threads 8 --timeout 0 main:app
