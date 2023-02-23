FROM python:3

COPY . /BOOKLAND

WORKDIR /BOOKLAND/library

RUN pip install -r /BOOKLAND/library/requirements.txt


EXPOSE 8000

CMD [ "python", "manage.py","runserver","127.0.0.1:8000"]