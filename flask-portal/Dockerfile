FROM python:3.8-buster

WORKDIR /flask-portal

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile

COPY app app
COPY tests tests
RUN python -m unittest

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]