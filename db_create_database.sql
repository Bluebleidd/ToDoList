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