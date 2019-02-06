============================================================================
============================================================================
Python MySQL Query==========================================================
http://www.mysqltutorial.org/python-mysql-query/ ===========================
============================================================================
1. This tutorial shows you how to query data from a MySQL database in Python by using MySQL 
Connector/Python API such as fetchone() , fetchmany() , and fetchall() .

To query data in a MySQL database from Python, you need to do the following steps:

- Connect to the MySQL Database, you get a MySQLConnection object.
- Instantiate a  MySQLCursor object from the the MySQLConnection object.
- Use the cursor to execute a query by calling its  execute() method.
- Use fetchone() ,  fetchmany() or  fetchall() method to fetch data from the result set.
- Close the cursor as well as the database connection by calling the  close() method of the corresponding object.

- We will show you how to use fetchone() , fetchmany() , and  fetchall() methods in more detail in the 
following sections.

2. Querying data with fetchone

The  fetchone() method returns the next row of a query result set or None in case there is no row left. 
Let’s take a look at the following code:

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
 def query_with_fetchone():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
 
        row = cursor.fetchone()
 
        while row is not None:
            print(row)
            row = cursor.fetchone()
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    query_with_fetchone()

Let’s examine the code in detail:

- First, we connected to the database by create a new  MySQLConnection object
- Second, from the  MySQLConnection object, we instantiated a new  MySQLCursor object
- Third, we executed a query that selects all rows from the books table.
- Fourth, we called  fetchone() method to fetch the next row in the result set. In the  while loop block,
we printed out the content of the row and move to the next row until all rows are fetched.
- Fifth, we closed both cursor and connection objects by invoking the  close() method of the corresponding 
object.


3. Querying data with fetchall

In case the number of rows in the table is small, you can use the  fetchall() method to fetch all rows 
from the database table.  See the following code.

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
 
def query_with_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
 
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    query_with_fetchall()
	
The logic is similar to the example with the  fetchone() method except for the  fetchall() 
method call part. Because we fetched all rows from the books table into the memory, we can 
get the total rows returned by using the  rowcount property of the cursor object.

4. Querying data with fetchmany

- For a relatively big table, it takes time to fetch all rows and return the result set. 
In addition,  fetchall() needs to allocate enough memory to store the entire result set 
in the memory. This is inefficient and not a good practice.
- MySQL Connector/Python provides us with the  fetchmany() method that returns the next number of 
rows (n) of the result set, which allows us to balance between time and memory space. Let’s take 
a look at how do we use  fetchmany() method.
- First, we develop a generator that chunks the database calls into a series of  fetchmany() 
calls as follows:

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

Second, we can use the  iter_row() generator to fetch 10 rows at a time as shown below:

def query_with_fetchmany():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
 
        cursor.execute("SELECT * FROM books")
 
        for row in iter_row(cursor, 10):
            print(row)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
	
