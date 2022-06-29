# Talent-Pool
This project is a simple and convenient talent pool developed by TUMTICS, utilizing `Airtalble` as its storage space. 

## Prerequisite

* [Airtable](https://airtable.com/)
* python_version >= "3.8"

## Set Up

### Environmental Variable

Create the `.env` file: 

```shell
export AIRTABLE_API_KEY=XXXXXXXXXXXXXXXXX
export AIRTABLE_BASE_ID=XXXXXXXXXXXXXXXXX
export FLASK_APP=<Server Name>      # For Example: app.dummy_server
export FLASK_ENV=development        # Default: production
```

## Deployment

### Docker-Compose

```shell
$ docker-compose up --build
$ docker-compose down
```

## Development

### flask-portal

```
$ cd ./flask-portal
```

#### Package Download and Switch Environment

```
$ pipenv install --dev
$ pipenv shell
```

#### Unit Test

```shell
$ python -m unittest                             # Test all scripts
$ python -m unittest tests/test_dummy_server.py  # Test a script
```

#### Run

```shell
$ python app/dummy_server.py
```

## References

* [Python Application Layouts: A Reference – Real Python](https://realpython.com/python-application-layouts/)
* [Testing Python in Visual Studio Code](https://code.visualstudio.com/docs/python/testing)
* [Getting Started — pyAirtable documentation](https://pyairtable.readthedocs.io/en/latest/getting-started.html)
* [Welcome to Flask — Flask Documentation (2.1.x)](https://flask.palletsprojects.com/en/2.1.x/)
