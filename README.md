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





Deployment
===========================

We use capistrano for deployment. 

This should be taken care of in the deploy directory through the Gemfile. Just run

	bundle install

inside your root directory (the one that has the Gemfile in it) to get capistrano.

After that, you should be able to do

	cap deploy

to deploy the code to the server. This is untested on machines other than Josh's right now.



Changing The Site: Instructions
===========================
To change anything to the site, you should be able to just edit the file, then do 

	git add [files you changed]; git commit -m "[some message about your commit]"
	git push
	cap deploy

Note the above about cap deploy being untested on many machines.

If you are adding a new page to the site, there are several things involved in this. The first thing you'll need to do is edit the lightcastle/urls.py The django framework will search through this file in order until it reaches the appropriate url, which are done as regular expressions. So in that file you'll see url('r^about/josh'.....) etc. After that you'll see 'r^about' ...  You have to haveit this way because if r^about was first, django would never get to r^(name) and you would therefore only have one about page. 

A basic page should look something like this 

  {% extends "subpage.html" %}
  {% block title %}~~PAGE TITLE HERE~~{% endblock %}
  {% block section %}2_sysadmin{% endblock %}
  {%block level%}2{%endblock%}
  {% block page%}sysadmin{% endblock %}
  {% block content %}
  <link rel="stylesheet" href={{ STATIC_URL }}main.css />
  <div id="content_container">
      ~~HTML CONTENT GOES HERE~~
      {%include "~~stories/sa_stories.html~~~~this is where you can include other html files.  "%}
  </div>
  {% endblock %}









