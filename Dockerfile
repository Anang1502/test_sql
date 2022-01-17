FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

RUN apt-get update ##[edited]

COPY ./ /app
EXPOSE 5016
CMD ["python3", "app.py"]