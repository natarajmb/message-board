# Message Board application built on Flask

This is a friendly message board flask application. Its python learning project from here https://realpython.com/flask-project/.
Application is exactly from tutorial expect that underlying database has been changed from SQLite to PostgresSQL

Application can be run locally or remotely on Kubernetes cluster. Remote run has dependency on Tanzu Application Platform.

## Running on Tanzu Application Platform (TAP)

### Pre-requisites

- Tanzu CLI 
- kubectl
- Tilt
- Optional IntelliJ or VSCode (Tanzu Plugins) for debugging
- Class Claim (database to bind) 

Configured access to Kubernetes cluster running TAP.

#### Create Claim

````bash
tanzu service class-claim create pgsql-1 --class postgresql-unmanaged --parameter storageGB=1
````

#### Run the application

````bash
tilt up
````
Follow the output from `tilt up` and browse the app. 

If you are using either Intellij or VSCode you can right-click on the project space and run `Tanzu Live Update`, which
will start the tilt process similar to `tilt up` but you have nicer dashboards to dig deep in.  


## Running Locally

### Pre-requisites

- PostgresSQL  
- Environment file (.env)

#### Start database service

Run postgres as docker container
````bash
docker run --name message-board-postgres -e POSTGRES_USER=board_user -e POSTGRES_DB=board -e POSTGRES_PASSWORD=secret! -p 5432:5432 -d postgres
````
#### Create environment file 

Copy the `env_sample` file and update it with your environment properties


### Building & Running an app

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


### Miscellaneous commands

To export out installed packages to requirements.txt
````bash
python -m pip freeze > requirements.txt
````

To change running port and to run in debug
````bash
python -m flask --app broad run --port 9090 --debug
````


