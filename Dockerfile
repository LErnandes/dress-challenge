FROM python:3.9.9-alpine3.15

RUN pip3 install --upgrade pip
COPY requirements.txt .

RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]