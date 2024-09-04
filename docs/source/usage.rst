Usage
=====

.. _installation:

Installation
------------

1. Clone Renale Server repo

.. code-block:: console

   (.venv) $ git clone https://github.com/Renale-Messenger/Renale-Server.git
   (.venv) $ cd renale-server

2. Install requirements (ensure you have python 3.9 or higher)

.. code-block:: console

   (.venv) $ pip install -r ./requirements.txt

3. Set up sqlite db(and config config.py file)

.. code-block:: sqlite

   sqlite> CREATE TABLE users(
   (x1...> id INT,
   (x1...> name TEXT,
   (x1...> sessions TEXT,
   (x1...> password TEXT,
   (x1...> token TEXT
   (x1...> );

   sqlite> CREATE TABLE messages(
   (x1...> id INT,
   (x1...> user TEXT,
   (x1...> chat TEXT,
   (x1...> text TEXT,
   (x1...> time REAL
   (x1...> );

   sqlite> CREATE TABLE chats(
   (x1...> is_group INT,
   (x1...> chat_id INT,
   (x1...> title TEXT,
   (x1...> description TEXT,
   (x1...> token TEXT,
   (x1...> members TEXT,
   (x1...> admins TEXT
   (x1...> );
   sqlite> .save renale.db

4. Run as module

.. code-block:: console

   (.venv) $ python -m app
-----------------
