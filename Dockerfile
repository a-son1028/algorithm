FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app

COPY api/requirements.txt api/requirements.txt
RUN pip3 install -U -r api/requirements.txt

COPY . .

EXPOSE 5000

CMD python3 api/api.py
