# Message Board application built on Flask

This is a friendly message board flask application. Its python learning project from here https://realpython.com/flask-project/.
Application is exactly from tutorial expect that underlying database has been changed from SQLite to PostgresSQL

## Pre-requisites

- PostgresSQL  
- Environment file (.env)

### Start database service

Run postgres as docker container
````bash
docker run --name message-board-postgres -e POSTGRES_USER=board_user -e POSTGRES_DB=board -e POSTGRES_PASSWORD=secret! -p 5432:5432 -d postgres
````
### Create environment file 

Copy the `env_sample` file and update it with your environment properties


## Building & Running an app

Create a python virtual environment
````bash
python -m venv venv
````
_NOTE: If you are using IntelliJ create the virtual environment from IDE._

Activate the environment
````bash
. venv/bin/activate
````

Install the required packages
````bash
python -m pip install -r requirements.txt
````

Create the necessary schema in the database
````bash
 python -m flask --app board init-db-pgsql
````

Run the application
````bash
python -m flask --app board run
````


## Miscellaneous commands

To export out installed packages to requirements.txt
````bash
python -m pip freeze > requirements.txt
````

To change running port and to run in debug
````bash
python -m flask --app broad run --port 9090 --debug
````


