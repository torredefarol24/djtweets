<h2>Install</h2>

- Install Python3.6
```
Check Ubuntu Docs
```

- Install pipenv
```
python3 -m pip install pipenv
```

- Create Dir
```
mkdir PROJ_NAME && cd PROJ_NAME
```

- Install Django
```
pipenv install --python3.6 django==2.2
```

-------

<h2>Setup Project</h2>

- Activate Virtual Environment
```
pipenv shell
```

- Create Django Project
```
django-admin startproject NAME_OF_PROJ .
```

- Create Django App
```
python3 manage.py startapp NAME_OF_APP
```

- INCLUDE in <strong>settings.py</strong>
```
INSTALLED_APPS = [
    'NAME_OF_APP'
]
```

- Run App
```
python3 manage.py runserver 8333
```

-----
<h2>Database Connection</h2>

- Provide DB Credentials in <strong>settings.py</strong>
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "DB_NAME",
        'USER': "DB_USER",
        'PASSWORD' : "DB_PASS",
        'HOST': "DB_HOST",
        'POST': "DB_PORT"
    }
}
```

- Migrate
```
python3 manage.py migrate
```

- Create Model in <strong>models.py</strong>
```
```

- Make Migrations
```
python3 manage.py makemigrations
```
-----

<h2> Include Templates</h2>

- Create Templates Folder & Include in <strong>settings.py</strong>

```
TEMPLATES = [
      {
            
            'DIRS': [os.path.join(BASE_DIR, "templates")],
      },
]
```


----
<h2>Routes & Functions</h2>

- Create Routes in <strong> urls.py</strong> 
- Create Controller Funcs in <strong> views.py</strong>

----

- Install Django Rest Framework
```
pipenv install djangorestframework
```

- INCLUDE in <strong>settings.py</strong>
```
INSTALLED_APPS = [
    'rest_framework'
]
```