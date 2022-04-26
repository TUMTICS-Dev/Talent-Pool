# Talent-Pool
The self-developed talent pool of TUMTICS, using Airtalble as its storage space. 

## Prerequisite

* python_version >= "3.8"
* [Airtable](https://airtable.com/)

## Set Up

### Environmental Variable

Create the .env file: 

```shell
AIRTABLE_API_KEY=XXXXXXXXXXXXXXXXX
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

## References

* [Python Application Layouts: A Reference – Real Python](https://realpython.com/python-application-layouts/)
* [Testing Python in Visual Studio Code](https://code.visualstudio.com/docs/python/testing)
* [Getting Started — pyAirtable documentation](https://pyairtable.readthedocs.io/en/latest/getting-started.html)