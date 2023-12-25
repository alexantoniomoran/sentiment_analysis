FROM python:3.9-slim

RUN mkdir /app
RUN cd /app/
COPY . /app

WORKDIR /app
RUN pip install -r requirements.txt

CMD ["sh", "./run.sh"]
