# **EmailVerifier**

## About
This is a pet-project, it should not be used for commercial purposes!<br/>

### Technology stack:
* Python 3.11;
* Django 4.2;
* HTML & CSS.

### Getting Started

#### 1. Create your '.env' file
* Create '.env' file in 'src' directory;
* Declare your environment variables in .env;
* File must contain: API_KEY, POSTGRES_PASSWORD, POSTGRES_USER, SECRET_KEY;
  * For example: API_KEY="this should be your API key".

#### 2. Set up Hunter API
* Сreate an account at [Hunter.io](https://hunter.io/);
* [Here will be your API_KEY](https://hunter.io/api-keys);
* Copy API_KEY to '.env'.

#### 3. Set up DB
* Create database 'email_verifier' in PostgreSQL;
* Declare your environment variables in .env;
* File must contain: POSTGRES_PASSWORD, POSTGRES_USER;
* Change HOST or PORT, as needed.

#### 3. Install requirements and start the server.
* `$ pip install -r requirements.txt`;
* `$ python manage.py makemigrations`;
* `$ python manage.py migrate`;
* `$ python manage.py runserver`.

Made by `Self`.