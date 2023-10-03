FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV MASTO_TOKEN setme
ENV PYTHONUNBUFFERED 1
CMD [ "python", "./bot.py" ]

