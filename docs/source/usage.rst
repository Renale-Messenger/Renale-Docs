Usage
=====

.. _installation:

Installation
------------

1. Clone Renale Server repo

.. code-block:: console

   git clone https://github.com/Renale-Messenger/Renale-Server.git
   cd renale-server

2. Install requirements (ensure you have python 3.9 or higher)

.. code-block:: console

   pip install -r ./requirements.txt

3. Set up sqlite db(and config config.py file)

.. code-block:: console

   CREATE TABLE users(
     id INT,
     name TEXT,
     sessions TEXT,
     password TEXT,
     token TEXT
   );

   CREATE TABLE messages(
     id INT,
     user TEXT,
     chat TEXT,
     text TEXT,
     time REAL
   );

   CREATE TABLE chats(
     is_group INT,
     chat_id INT,
     title TEXT,
     description TEXT,
     token TEXT,
     members TEXT,
     admins TEXT
   );

   .save renale.db

4. Run as module

.. code-block:: console

   python -m app
-----------------
