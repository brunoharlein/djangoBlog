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
- Configuration de la variable DATABASES dans setting.py
- DATABASES = {
    - 'default': {
        - 'ENGINE': 'django.db.backends.postgresql',
        - 'NAME': 'blog',
        - 'USER': 'blogAdmin',
        - 'PASSWORD': '1234',
        - 'HOST': 'localhost',
        - 'PORT': '5432',
    - }
- }
- localhost = 127.0.0.1 (adresse ip locale de l'ordinateur)
- création d'une application 'posts' pour la gestion des articles du blog
- Dans le dossier src : python manage.py startapp posts (un dossier posts est présent)
- Ajout de l'application dans le fichier setting.py variable INSTALLED_APPS ligne 38 'posts'
- Dans le fichier models.py de l'application posts nous allons créer un modèle pour sauvegarder nos articles dans la database
- class BlogPost(models.Model):
- Nous allons rajouter quelques informations sur le modèle, notamment une classe Meta qui va nous permettre de modifier 
  l'ordre d'affichage par défaut des articles dans l'interface d'administration ainsi que le nom affiché (par défaut, l'interface afficherait le nom du modèle, donc BlogPost)
- ajout de la méthode __str__ pour utiliser le titre des articles
- ajout du slug automatiquement en fonction du titre de l'article. Si aucun slug n'est indiqué par l'auteur de l'article, on utilise slugify sur le titre de l'article pour en générer un automatiquement
- Maintenant que notre modèle est créé, nous allons pouvoir créer les migrations et les appliquer pour créer les tables dans la base de données de notre projet.
- Nous allons ainsi également appliquer les migrations de base de Django qui vont créer les tables pour la gestion des utilisateurs.
- python manage.py makemigrations et python manage.py migrate
- Ajout du modèle dans l'interface administration.
- Avant d'ajouter le modèle, nous allons déjà créer un utilisateur admin pour nous connecter à l'interface d'administration. C'est également avec cet utilisateur que nous signerons les articles (dans ce projet, nous ne gérons pas la possibilité d'ajouter plusieurs auteurs. Le seul auteur des articles sera donc l'utilisateur admin).
- Pour ça, nous allons utiliser la commande : python manage.py createsuperuser 
- Nous avons un utilisateur, maintenant il est temps de se connecter à l'interface admin 
- python manage.py runserver
- sauf que pas d'articles pour l'instant ... pas possible d'en ajouter également 
- Il faudra ajouter les modèles que nous souhaitons afficher dans admin.py dossier posts
- Une fois les modèles ok vous pouvez lancer le runserver et commencer vos articles, le CRUD est en place !!
- En route pour du HTML ! création dans SRC d'un dossier templates qui contiendra les fichiers communs à notre projet et non à une application en particulier.
- Dans le dossier templates création du fichier base.html.
- Il serait bien que Django trouve ce fichier ! Il faut donc modifier le settings.py à la variable : TEMPLATES
- Dans le fichier base.html, nous insérons les balises HTML qui seront communes à toutes nos pages, ainsi que deux blocs dans lesquels nous insérerons des données par la suite (un bloc title pour le titre de la page et un bloc content pour le contenu)



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



