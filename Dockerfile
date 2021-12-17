#Dockerfile 

FROM python:3.8

WORKDIR app

ENV FLASK_APP=app.py

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_ENV=development

CMD ["python", "steam.py", "--host", "0.0.0.0"]