============================================================================
============================================================================
Python Connecting to MySQL Databases =======================================
http://www.mysqltutorial.org/python-connecting-mysql-databases/ ============
============================================================================
1. Preparing a sample database

First, we create a new database named  python_mysql for demonstration through the tutorials.
To create a new database, you can launch the MySQL Workbench or mysql client tool, and use the 
CREATE DATABASE statement as follows :
CREATE DATABASE python_mysql;
Second, you need to load the sample data into the  python_mysql database from python_mysql.sql file.

2. Connecting to MySQL database using connect() function
Let’s take a look at the following Python module ( python_mysql_connect1.py )

import mysql.connector
from mysql.connector import Error
 
 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='root',
                                       password='secret')
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        conn.close()
 
 
if __name__ == '__main__':
    connect()

Let’s examine this module in detail:

- First, we imported  mysql.connector and Error objects from the MySQL Connector/Python package.
- Second, to connect to MySQL database, we used connect() function that accepts parameters: host, 
database, user and password. The  connect() function established a connection to the  python_mysql 
database and returns a MySQLConnection object.
- Third, we checked if the connection to the MySQL database has been established successfully by using  
is_connected() method. In case an exception occurs e.g., database server is not available, database does 
not exist, or invalid user name or password, etc., Python will raise an  Error exception. We handled this 
exception by using the  try except block.
- Fourth, if no exception occurred, we closed the database connection by calling the  close() method of 
the  MySQLConnection object.

3. Connecting to MySQL Database using MySQLConnection object

In this example, we create a database configuration file named  config.ini and define a section with four 
parameters as follows:

[mysql]
host = localhost
database = python_mysql
user = root
password =

We can create a new module named  python_mysql_dbconfig.py that reads the database configuration from the  
config.ini file and returns a dictionary as follows:

from configparser import ConfigParser
 
 
def read_db_config(filename='config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)
 
    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
 
    return db
	

Notice that we used ConfigureParser package to read the configuration file.
Let’s test this module in the REPL:

>>> from python_mysql_dbconfig import read_db_config
>>> read_db_config()
{'password': '', 'host': 'localhost', 'user': 'root', 'database': 'python_mysql'}

It works as expected.
Now, we can create a new module python_mysql_connect2.py , which uses the MySQLConnection object to connect to 
the python_mysql database.

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
 
def connect():
    """ Connect to MySQL database """
 
    db_config = read_db_config()
 
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')
 
    except Error as error:
        print(error)
 
    finally:
        conn.close()
        print('Connection closed.')
 
 
if __name__ == '__main__':
    connect()
	

Let’s examine the code above in a greater detail:

- First, we imported necessary objects including MySQLConnection , Error from MySQL Connector/Python
 package and  read_db_config from  python_mysql_dbconfig module that we’ve developed.
- Second, inside the  connect() function, we read the database configuration and used it to create a 
new instance of MySQLConnection object. The rest of the code works similar to the first example.

When we run the  python_mysql_connect2 in the console window, we get the following output:

>python python_mysql_connect2.py
Connecting to MySQL database...
connection established.
Connection closed.


In this tutorial, we have shown you how to connect to MySQL databases using  connect() function 
and MySQLConnection object. Both ways have the same effect that establishes a connection to the 
MySQL database and return a MySQLConnection object.





