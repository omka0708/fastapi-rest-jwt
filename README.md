# fastapi-rest-jwt

Async authentication API (by JWT token) + async migrations.
Used stack: *FastAPI*, *PostgreSQL*, *asyncio*, *Kubernetes*.

## Install

Install `fastapi-rest-jwt` from source:

    git clone https://github.com/omka0708/fastapi-rest-jwt
    cd fastapi-rest-jwt

You should have `.env` file at the */fastapi-rest-jwt* folder.

Environment file `.env` should contain:
    
    DB_USER=<db_username>
    DB_PASS=<db_password>
    DB_HOST=rest-jwt-db
    DB_PORT=5432
    DB_NAME=<db_name>
    PGADMIN_EMAIL=<pgadmin_mail>
    PGADMIN_PASSWORD=<pgadmin_pass>
    SECRET_AUTH=<some_string>

## Run app

Run this command at the working directory */fastapi-rest-jwt*:

    docker compose up -d --build

## Documentation

You can see documentation at:

    GET localhost:8000

It will redirect you to API documentation. 
