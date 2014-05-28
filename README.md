Whisky DB
=========

Installation
------------

 1. ** CREATE A VIRTUAL ENVIRONMENT **
 2. Clone Code
 2. Install requirements
 3. Generate database
 4. Run migrations

    virtualenv whiskydb
    cd whiskydb/
    source bin/activate

    git clone ... whiskydb
    cd whiskydb/
    pip install -r requirements.txt

    ./manage.py syncdb
    ./manage.py migrate
    ./manage.py runserver
