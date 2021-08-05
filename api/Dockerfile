FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -U -r requirements.txt

COPY . .

EXPOSE 5000

CMD python3 api.py
