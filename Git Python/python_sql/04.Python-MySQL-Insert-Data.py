============================================================================
============================================================================
Python MySQL Insert Data====================================================
http://www.mysqltutorial.org/python-mysql-insert/ ==========================
============================================================================
In this tutorial, you will learn how to insert data into MySQL table using MySQL Connector/Python API.

To insert new rows into a MySQL table, you follow the steps below:

- Connect to the MySQL database server by creating a new MySQLConnection object.
- Initiate a MySQLCursor object from the MySQLConnection object.
- Execute the INSERT statement to insert data into the intended table.
- Close the database connection.

MySQL Connector/Python provides API that allows you to insert one or many rows into a table at a time. 
Let’s examine at each method in more detail.

1. Insert one row into a table
The following code inserts a new book into the  books table:

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def insert_book(title, isbn):
    query = "INSERT INTO books(title,isbn) " \
            "VALUES(%s,%s)"
    args = (title, isbn)
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
   insert_book('A Sudden Light','9781439187036')
 
if __name__ == '__main__':
    main()


In the above code:
- First, we import MySQLConnection and Error objects from the MySQL Connector/Python package and 
read_db_config() function from the python_mysql_dbconfig module.
- Second, we define a new function named insert_book() that accepts two arguments: title and isbn. 
Inside the insert_book() function, we prepare an  INSERT statement (query) and data (args) that we will
insert into the books table. Notice that the data we passed into the function is a tuple.
- Third, inside the  try except block, we create a new connection, execute the statement, and 
commit the change. Note that you have to call the  commit() method explicitly in order to make 
the changes to the database. In case a new row is inserted successfully, we can retrieve the last 
insert id of the AUTO_INCREMENT column by using the  lastrowid property of the MySQLCursor object.
- Fourth, at the end of the  insert_book() function, we closed the cursor and database connection.
- Fifth, inside the  main() function, we call the  insert_book() function and pass the  title and  
isbn to insert a new row into the  books table.









