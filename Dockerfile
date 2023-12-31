FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080


RUN python ./proj/manage.py


CMD ["gunicorn", "-b", "0.0.0.0:8080", "core.wsgi:application"]
