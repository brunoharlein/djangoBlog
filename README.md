# DjangoBlog

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)  

Blog sous Django pour débuter

## Pour commencer

Création d'un dossier, installation d'un ENV, de Django puis création du blog 

- pip install Django==3.2.4
- pip install psycopg2-binary (pour mac)
- django-admin startproject blog
- psql
- create database blog;
- création d'un utilisateur (juste pour cette database) : CREATE USER blogadmin WITH ENCRYPTED PASSWORD '1234'
- Une fois l'utilisateur créé, il faudra modifier des paramètres pour utiliser l'utilisateur et la database avec Django
- lien vers la doc Django : https://docs.djangoproject.com/fr/3.1/ref/databases/#optimizing-postgresql-s-configuration
- ALTER ROLE blogadmin SET client_encoding TO 'utf8';
- ALTER ROLE blogadmin SET default_transaction_isolation TO 'read committed';
- Les accés à notre utilisateur : GRANT ALL PRIVILEGES ON DATABASE blog TO blogadmin;


### Pré-requis

Ce qui est requis pour commencer avec votre projet...

- Python 3.9
- Git
- Un IDE ;-)

## Fabriqué avec

* Python 3.9
* Django 3.2.4
* Pycharm
* Psycopg2
* PostgreSQL

## Auteurs

-Bruno Harlein



