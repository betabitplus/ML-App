FROM python:3.7.2

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "app.py"]
