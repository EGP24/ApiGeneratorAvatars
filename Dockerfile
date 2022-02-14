FROM python:3.8
WORKDIR /project
COPY requirements.txt .
COPY /core ./core
COPY /db ./db
COPY /handlers ./handlers
COPY /schemas ./schemas
COPY /services ./services
COPY /.env .
COPY /main.py .
RUN pip install -r requirements.txt
