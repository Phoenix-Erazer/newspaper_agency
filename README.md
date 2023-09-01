# Newspaper agency

Django project for managing newspaper and redactors in newspaper agency

## Check it out!

[Newspaper agency project deployed to Haroky](PASTE_LINL_HERE)

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/Phoenix-Erazer/newspaper_agency
$ cd newspaper_agency
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ python -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`.
