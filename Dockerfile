# Dockerfile - this is a comment. Delete me if you want.
FROM python:stretch AS base
RUN apt-get update
RUN apt-get install unixodbc-dev -y
WORKDIR /app
EXPOSE 6000

FROM python:stretch AS build
COPY ["requirements.txt","."]
WORKDIR /packages
RUN pip download -r /requirements.txt

FROM base AS final
WORKDIR /app/packages/
COPY --from=build /packages .
RUN pip install --no-index --find-links=/packages/ /app/packages/*
WORKDIR /app
COPY . .

ENTRYPOINT ["python", "app.py"]
