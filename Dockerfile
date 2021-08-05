FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -U -r requirements.txt

ENV FLASK_APP=api.py

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]

