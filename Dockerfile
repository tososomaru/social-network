FROM python:3.8-slim
#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./migrations /app/migrations
COPY ./alembic.ini /app/alembic.ini

COPY ./src /app/src

CMD ["ls"]

EXPOSE 8000

#CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]

