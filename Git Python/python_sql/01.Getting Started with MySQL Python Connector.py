============================================================================
============================================================================
Getting Started with MySQL Python Connector=================================
http://www.mysqltutorial.org/getting-started-mysql-python-connector/ =======
============================================================================
1. To access the MySQL database from Python, you need a database driver. 
MySQL Connector/Python is a standardized database driver provided by MySQL.

2. MySQL Connector/Python supports almost all features provided by MySQL version 5.7. 
It allows you to convert the parameter’s value between Python and MySQL data types e.g., 
Python datetime and MySQL DATETIME.

3. MySQL Connector/Python is designed specifically to MySQL. It supports all MySQL extensions 
to standard SQL such as LIMIT clause.

4. Download link : https://dev.mysql.com/downloads/connector/python/2.0.html

5. Installing MySQL Python connector
Installing MySQL Python connector is straightforward. For example, to install it in the Windows 
environment, you use the following steps:

-- Unpack the download file into a temporary directory e.g., C:\temp
-- Start a console window and switch to the folder where you unpack the connector

> cd c:\temp
Inside the c:\temp folder, use the following command:

c:\temp > python setup.py install

6. Verifying MySQL Connector/Python installation
After installing the MySQL Python connector, you need to test it to make sure that it is 
working correctly and you are able to connect to the MySQL database server without any issues. 
To verify the installation, you use the following steps:

1. Open Python command line
2. Type the following code


>>> import mysql.connector
>>> mysql.connector.connect(host='localhost',database='mysql',user='root',password

If the output is shown below, you have been successfully installing the MySQL Python connector in your system.

<mysql.connector.connection.MySQLConnection object at 0x0187AE50>
