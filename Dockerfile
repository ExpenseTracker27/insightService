FROM python:3.11-slim
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /code/app

ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]