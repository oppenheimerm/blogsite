# Blog built on Django

## Project Requirements

The [requirements.txt](./requirements.txt) has the following packages:

| Package | Description |
| ------- | ----------- |
| [Django](https://pypi.org/project/Django/) | Web application framework. |
| [pyscopg2-binary](https://pypi.org/project/psycopg-binary/) | PostgreSQL database adapter for Python. |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Read key-value pairs from .env file and set them as environment variables. In this sample app, those variables describe how to connect to the database locally. <br><br> This package is used in the [manage.py](./manage.py) file to load environment variables. |
| [whitenoise](https://pypi.org/project/whitenoise/) | Static file serving for WSGI applications, used in the deployed app. <br><br> This package is used in the [azureproject/production.py](./azureproject/production.py) file, which configures production settings. |
| [python-dotenv 0.20.0](https://pypi.org/project/python-dotenv/) | Python-dotenv reads key-value pairs from a .env file and can set them as environment variables. It helps in the development of applications following the 12-factor principles.
| [taggit](https://django-taggit.readthedocs.io/en/latest/) | Reusable Django application designed to make adding tagging to your project easy and fun.