FROM python

WORKDIR /my_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "app.py"]
