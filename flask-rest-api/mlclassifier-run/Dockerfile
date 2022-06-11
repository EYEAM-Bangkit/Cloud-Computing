FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt
RUN curl -sSL https://sdk.cloud.google.com | bash
RUN gsutil cp gs://BUCKET_NAME/path/to/file ./model/model_1.h5

EXPOSE 4000
CMD gunicorn -b 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 app:app
