# GilaSW - Code Challenge Gerardo Benitez
This is a project created to resolve the code challenge. 
The project is an API created using:

* FastAPI
* Docker
* SQLModel (SqlAchemy)
* RabbitMQ
* Celery
* PostgreSql / SQLite

## Requirements

Python 3.9+

## Project

### Setup environment
1. copy .env.example to .env
2. set environment variables

### Run It: option 1 with docker

1. Start the project 

```sh
docker-compose up
```

### Run It: option 2 

2. Go to [http://localhost:9009/api/ping](http://localhost:9009/api/ping).

## Architecture

![image info](./static/images/arquitecture.png)

## Database

![image info](./static/images/database.png)
