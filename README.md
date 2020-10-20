# BIGCORP API
## QUICK SETUP
* If you wish to run your own build, first ensure you have Python and Heroku globally installed in your computer. If not, you can get python [here](https://www.python.org) and Heroku [here](https://devcenter.heroku.com/articles/heroku-cli).
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/tip-2020-c1-grupo1/refugio-backend.git
    ```
* #### Defaults
    By default the setup is using sqlite, the docker setup uses postgresql
* #### Steps
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd refugio-backend
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  env -p python3
            $ source env/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
            $ python manage.py createsuperuser
        ```
    5. Run It With Postgres - First configure your postgresql connections
    ```bash
        $ python manage.py runserver --settings=project.settings_postgres
    ```
    5b Run it with SQLite (default)
    ```bash
        $ python manage.py runserver
    ```

  
## Check with curl:
```bash
       curl 'http://localhost:8000/api/employees/?expand=department.super_department&limit=5&offset=30' -H 'Accept: application/json'
```


## ALSO CHECK THE SWAGGER API:
```bash
        http://localhost:8000/docs/
```



DOCKER CONFIGURATION

# Docker-compose-django-rest-deploy
Deploying a django based rest api with postgresql backend using docker-compose

###### 1. Create an empty project directory.
###### 2. Create a new file called Dockerfile in your project directory.
###### 3. Add the following content to the Dockerfile.
```
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
 
```
This Dockerfile starts with a Python 3 parent image. The parent image is modified by adding a new code directory.  
The parent image is further modified by installing the Python requirements defined in the requirements.txt file.  

###### 4. Save and close the Dockerfile.  
###### 5. Create a requirements.txt in your project directory.  

This file is used by the RUN pip install -r requirements.txt command in your Dockerfile.  

###### 6. Add the required software in the file.  

###### 7. Save and close the requirements.txt file.  

###### 8. Create a file called docker-compose.yml in your project directory.

The docker-compose.yml file describes the services that make your app. In this example those services   
are a web server and database. The compose file also describes which Docker images these services use,   
how they link together, any volumes they might need mounted inside the containers. Finally, the   
docker-compose.yml file describes which ports these services expose. See the docker-compose.yml   
reference for more information on how this file works.  

###### 9. Add the following configuration to the file.  

```
version: '3'

services:
  db:
    image: postgres
  web:
    build: .
    command: python3 manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
```

This file defines two services: The db service and the web service.  

###### 10. Save and close the docker-compose.yml file.  

## Connect the database  

###### 1. In your project directory, edit the project/settings_postgres.py file.  

###### 2. Replace the DATABASES = ... with the following:  

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

```

These settings are determined by the postgres Docker image specified in docker-compose.yml.    

###### 3. Save and close the file.  
###### 4. Run the docker-compose up command from the top level directory for your project.  

```
$ docker-compose up
djangosample_db_1 is up-to-date
Creating djangosample_web_1 ...
Creating djangosample_web_1 ... done
Attaching to djangosample_db_1, djangosample_web_1
db_1   | The files belonging to this database system will be owned by user "postgres".
db_1   | This user must also own the server process.
db_1   |
db_1   | The database cluster will be initialized with locale "en_US.utf8".
db_1   | The default database encoding has accordingly been set to "UTF8".
db_1   | The default text search configuration will be set to "english".

. . .

web_1  | May 30, 2017 - 21:44:49
web_1  | Django version 1.11.1, using settings 'project.settings_postgres'
web_1  | Starting development server at http://0.0.0.0:8000/
web_1  | Quit the server with CONTROL-C.
```

At this point, your Django app should be running at port 8000 on your Docker host.   
On Docker for Mac and Docker for Windows, go to http://localhost:8000 on a web browser to see   
the Django welcome page.

NOTE: for creating super user for django project use the script provided at the management/commands/createsu.
NOTE: Modify the database settings in <Django-project>/settings.py

