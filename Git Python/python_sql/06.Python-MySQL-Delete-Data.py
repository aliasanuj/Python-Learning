============================================================================
============================================================================
Python MySQL Delete Data====================================================
http://www.mysqltutorial.org/python-mysql-delete-data/ =====================
============================================================================
In this tutorial, we will walk you through steps of deleting data in MySQL database 
by using MySQL Python.

To delete rows in a MySQL table from Python, you need to do the following steps:
- Connect to the database by creating a new MySQLConnection object.
- Instantiate a new cursor object and call its  execute() method. To commit the changes, 
you should always call the  commit() method of the MySQLConnection object after calling the  execute() method.
- Close the cursor and database connection by calling  close() method of the corresponding objects.

The following example shows you how to delete a book specified by book id:

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def delete_book(book_id):
    db_config = read_db_config()
 
    query = "DELETE FROM books WHERE id = %s"
 
    try:
        # connect to the database server
        conn = MySQLConnection(**db_config)
 
        # execute the query
        cursor = conn.cursor()
        cursor.execute(query, (book_id,))
 
        # accept the change
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
if __name__ == '__main__':
    delete_book(102)

- Notice that we use the  read_db_config() function from the python_mysql_dbconfig module that we 
developed in the previous tutorial.
- Because we need to delete a specific row in the  books table, we need to put a placeholder (%) in side 
the DELETE statement.
- When we call the  execute() method, we pass both DELETE statement and  (book_id,) tuple. The connector 
will translate the  DELETE statement into the following form:

DELETE FROM books WHERE id = 102

- You should always use placeholders inside any query that you pass to the  execute() method. 
This helps you prevent SQL injection.
- Before running the code, let’s check the  books table to see the data before we delete the entry.

SELECT * FROM books
WHERE id = 102;

id		title		isbn
102		bookname	12412424

After running the module above, we execute the SELECT statement again. No rows returned. 
It means the module has deleted the entry successfully.








