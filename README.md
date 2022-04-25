# Talent-Pool
The self-developed talent pool of TUMTICS

## Prerequisite

* python_version >= "3.7"

## Set Up

### Environmental Variable

Create the .env file: 

```shell
AIRTABLE_API_KEY=XXXXXXXXXXXXXXXXX
```

## Deployment

### Package Management

```shell
$ pipenv lock -r > requirements.txt
$ mv requirements.txt ./app
```

### Docker-Compose

```shell
$ docker-compose up --build
$ docker-compose down
```

## Development

### Package Download

```
$ pipenv install --dev
```

### Unit Test

```shell
$ python -m unittest                             # Test all scripts
$ python -m unittest tests/test_dummy_server.py  # Test a script
```

## References

* [Python Application Layouts: A Reference – Real Python](https://realpython.com/python-application-layouts/)
* [Testing Python in Visual Studio Code](https://code.visualstudio.com/docs/python/testing)
* [Getting Started — pyAirtable documentation](https://pyairtable.readthedocs.io/en/latest/getting-started.html)