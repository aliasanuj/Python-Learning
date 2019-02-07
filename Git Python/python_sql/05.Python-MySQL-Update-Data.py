============================================================================
============================================================================
Python MySQL Update Data====================================================
http://www.mysqltutorial.org/python-mysql-update/ ==========================
============================================================================
Summary: this tutorial walks you through steps required to update data in MySQL table by using 
MySQL Connector/Python API.

To update data in a MySQL table in Python, you follow the steps below:

- Connect to the database by creating a new MySQLConnection object.
- Create a new MySQLCursor object from the MySQLConnection object and call the execute() method of the 
MySQLCursor object. To accept the changes, you call the commit() method of the MySQLConnection object 
after calling the execute() method. Otherwise, no changes will be made to the database.
- Close the cursor and database connection.

In the following example, we will update the title of a book specified by a book id:

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
 
def update_book(book_id, title):
    # read database configuration
    db_config = read_db_config()
 
    # prepare query and data
    query = """ UPDATE books
                SET title = %s
                WHERE id = %s """
 
    data = (title, book_id)
 
    try:
        conn = MySQLConnection(**db_config)
 
        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)
 
        # accept the changes
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    update_book(37, 'The Giant on the Hill *** TEST ***')

In this module, we used the read_db_config() function from the python_mysql_dbconfig module that 
we created in the connecting to database from Python tutorial.

We put two placeholders (%)  inside the UPDATE statement, one for book title and the other for book id. 
We passed both  UPDATE statement ( query ) and  (title,id) tuple to the  execute() method. The connector 
will interpret the query to the following:

UPDATE books
SET title = 'The Giant on the Hill *** TEST ***'
WHERE id = 37

It is important to understand that we should always use placeholders ( %s) inside any SQL statements 
that contain input from users. This helps us prevent SQL injection.

Let’s test our new module to see if it works.
First, we select the book with id 37:

SELECT * FROM books
WHERE id = 37;

id	title					isbn
37	The Giant on the Hill	12154424

Second, we run the module.
Third, we select the book entry by executing the  SELECT statement above again to see if it 
is really changed.

id	title									isbn
37	The Giant on the Hill *** TEST ***		12154424

It works as expected.
In this tutorial, you have learned how how to update data by using MySQL Connector/Python API.











