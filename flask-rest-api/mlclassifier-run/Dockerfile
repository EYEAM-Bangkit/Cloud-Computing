FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt
RUN gsutil cp 'gs://eyeam-model/model_1_inceptionv3 (2022_06_05-02-54-20-PM).h5' ./model/model_1.h5

EXPOSE 4000

CMD gunicorn -b 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 app:app
