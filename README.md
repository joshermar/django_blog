# Django Blog

A complete microblog web app that implements CRUD operations using Django with MySQL

## Instructions

The following instructions were tested on Ubuntu 18.04 using Python 3.6.7. 

### Initial Requirements

You must first set up a database to be used by the app. Install MySQL server (I also had to install libmysqlclient-dev).

Once you have MySQL installed, start up the SQL shell and a create a new user and database:

    CREATE DATABASE simple_blog;
    CREATE USER 'blog_user'@'localhost' IDENTIFIED BY 'blogpass';
    GRANT ALL PRIVILEGES ON simple_blog . * TO 'blog_user'@'localhost';

Now you want to set up your Python envronment using the following commands:
    
    python3 -m venv .env

To activate the environment, enter the following from the same directory:
    
    source .env/bin/activate

Now we need to install a few packages with pip:
    
    pip install django
    pip install django-crispy-forms
    pip install pillow
    pip install wheel
    pip install mysqlclient

### Setting up the blog

We're now ready to begin setting up the app. Enter the folling command to create the MySQL tables:
  
    ./manage.py migrate

Almost done. We just want to create a superuser to manage the app:
    
    ./manage.py createsuperuser

Finally, run the server using:

    ./manage.py runserver
