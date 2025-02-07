# ToDoList
Jest to prosta aplikacja do zarządzania zadaniami, która pozwala użytkownikom tworzyć tablice, dodawać zadania i śledzić postęp tych zadań. Aplikacja obsługuje uwierzytelnianie użytkowników (logowanie i rejestrację), kategoryzację zadań (Do Zrobienia, W Trakcie, Zrobione) oraz nawigację pomiędzy różnymi widokami, takimi jak tablice i zadania.

Używane technologie (zalecane wersje):
- Python (3.13.1)
- PostgreSQL (17.2)
- pgAdmin (8.13)

W programie pgAdmin4 należy:
1. Stworzyć użytkownika "ToDoUser":
   
      -- Role: "ToDoUser"
      -- DROP ROLE IF EXISTS "ToDoUser";
      CREATE ROLE "ToDoUser" WITH
        LOGIN
        NOSUPERUSER
        INHERIT
        NOCREATEDB
        NOCREATEROLE
        NOREPLICATION
        NOBYPASSRLS
        ENCRYPTED PASSWORD "<password>"
   
2. Stworzyć baze danych "ToDoDatabase":
   
      -- Database: ToDoDatabase
      -- DROP DATABASE IF EXISTS "ToDoDatabase";
      CREATE DATABASE "ToDoDatabase"
          WITH
          OWNER = "ToDoUser"
          ENCODING = 'UTF8'
          LC_COLLATE = 'English_United Kingdom.1252'
          LC_CTYPE = 'English_United Kingdom.1252'
          LOCALE_PROVIDER = 'libc'
          TABLESPACE = pg_default
          CONNECTION LIMIT = -1
          IS_TEMPLATE = False;

Zainstaluj pakiet umożliwiający aplikacji Python korzystać z zapytań PosthreSQL:
- > pip install psycopg2-binary

Po instalacji podanych technologii, w samym projekcie należy sprawdzić plik ToDOList/project/settings.py:
   DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'ToDoDatabase',    # Nazwa bazy danych
            'USER': 'ToDoUser',        # Nazwa użytkownika PostgreSQL
            'PASSWORD': '<password>',  # Hasło użytkownika PostgreSQL
            'HOST': 'localhost',
        }
    } 
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'

W terminalu należy przeprowadzić migracje:
- > python manage.py makemigrations
- > python manage.py migrate

(Opcjonalnie) Aby uzyskać dostęp do panelu administracyjnego:
- python manage.py createsuperuser

Po przeprowadzeniu migracji należy uruchomić serwer:
- > python manage.py runserver

Następnie można przetestować projekt pod adresem:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/admin (panel administracji)
