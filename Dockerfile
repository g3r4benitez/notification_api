FROM python:3.9

EXPOSE 9009

WORKDIR /code

# Install requirements.txt
COPY ./requirements.txt .
COPY ./.env .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app app

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "9009"]
