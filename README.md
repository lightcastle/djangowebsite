LightCastle Website
=============================
lightcastle site written in django

Setup (Ubuntu Specific)
=======================

Step 1: Install Python
-----------------------

    sudo apt-get update
    sudo apt-get install python2.7

Step 2: Install PIP
-----------------------

    sudo apt-get install python-pip
    sudo pip install -U pip

Step 3: Install Python MySQL drivers (assumes you have mysql installed)
-----------------------

    apt-get install python-dev libmysqlclient-dev
    pip install MySQL-python

Step 3a: Create MySQL database/user
----------------------

    create database djangotest
	grant usage on *.* to djangouser@localhost identified by 'djangopass';
    grant all privileges on djangotest.* to djangouser@localhost ;	
    

Step 4: Install django
-----------------------

    create database djangotest
	sudo apt-get install python-django

Step 5: Update Configuration
-------------------------

edit lightcastle/settings.py.examtp settings so that your email address is setup in the smtp settings.
save the file on your computer without the .example suffix.
    	
Step 6: Start up the web server
-----------------------
    
	cd lightcastle/
    python manage.py runserver

Visit http://localhost:8000






<h3>Deployment</h3>
===========================

We use capistrano for deployment. 

This should be taken care of in the deploy directory through the Gemfile. Just run

	bundle install

to get capistrano.



