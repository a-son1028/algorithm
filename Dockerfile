FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app

COPY api/requirements.txt api/requirements.txt
RUN pip3 install -U -r api/requirements.txt

ENV FLASK_APP=api.py

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]

