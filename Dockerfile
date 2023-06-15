FROM python:3.8.10

WORKDIR /code

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3","manage.py","runserver","0:8000"]