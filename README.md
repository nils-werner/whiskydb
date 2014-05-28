Whisky DB
=========

Installation
------------

Create virtual environment

    virtualenv whiskydb
    cd whiskydb/
    source bin/activate

Clone code and install requirements

    git clone ... whiskydb
    cd whiskydb/
    pip install -r requirements.txt

Install database and run migrations

    ./manage.py syncdb
    ./manage.py migrate
    ./manage.py runserver
