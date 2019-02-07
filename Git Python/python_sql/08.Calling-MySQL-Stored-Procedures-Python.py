============================================================================
============================================================================
Calling MySQL Stored Procedures in Python===================================
http://www.mysqltutorial.org/calling-mysql-stored-procedures-python/ =======
============================================================================
This tutorial shows you how to call MySQL stored procedures in Python using MySQL Connector/Python API.
Before we start
If you are not familiar with MySQL stored procedures or want to review it as a refresher, you can follow 
the MySQL stored procedures tutorial.

We will create two stored procedures for the demonstration in this tutorial. The first stored procedure gets all books with 
authors information from  books and  authors tables:

 
USE python_mysql$$
 
CREATE PROCEDURE find_all()
BEGIN
 SELECT title, isbn, CONCAT(first_name,' ',last_name) AS author
 FROM books
 INNER JOIN book_author ON book_author.book_id =  books.id
 INNER JOIN AUTHORS ON book_author.author_id = authors.id;
END$$
 
DELIMITER ;

The  find_all() stored procedure has a SELECT statement with JOIN clauses that retrieve title, isbn 
and author’s full name from  books and  authors tables. When we execute the  find_all() stored 
procedure, it returns a result as follows:

CALL find_all();

title		isbn		author 
hcbhxch		54545		dcnd djcdjc
cnjcjcb 	54554		mcjdndd jndvjdn
ndjncjv		48488		dkvnfj nfkvfdmvk

The second stored procedure named  find_by_isbn() that is used to find a book by its ISBN as follows:

DELIMITER $$
 
CREATE PROCEDURE find_by_isbn(IN p_isbn VARCHAR(13),OUT p_title VARCHAR(255))
    BEGIN
 SELECT title INTO p_title FROM books
 WHERE isbn = p_isbn;
    END$$
 
DELIMITER ;

The  find_by_isbn() accepts two parameters: the first parameter is isbn (IN parameter) and 
second is title (OUT parameter). When you pass the isbn to the stored procedure, you will 
get the title of the book, for example:

CALL find_by_isbn('1235927658929',@title);
SELECT @title;

Calling stored procedures from Python
To call a stored procedure in Python, you follow the steps below:

- Connect to MySQL database by creating a new MySQLConnection object.
- Instantiate a new MySQLCursor object from the MySQLConnection object by calling the cursor() 
method.
- Call  callproc() method of the MySQLCursor object. You pass the stored procedure’s name as 
the first argument of the  callproc() method. If the stored procedure requires parameters, 
you need to pass a list as the second argument to the  callproc() method. In case the stored 
procedure returns a result set, you can invoke the  stored_results() method of the MySQLCursor 
object to get a list iterator and iterate this result set by using the  fetchall() method.
- Close the cursor and database connection as always.


The following example demonstrates how to call the  find_all() stored procedure in Python and 
output the result set.

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def call_find_all_sp():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
 
        cursor.callproc('find_all')
 
        # print out the result
        for result in cursor.stored_results():
            print(result.fetchall())
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
if __name__ == '__main__':
    call_find_all_sp()
	
	
The following example shows you how to call the  find_by_isbn() stored procedure.

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def call_find_by_isbn():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
 
        args = ['1236400967773', 0]
        result_args = cursor.callproc('find_by_isbn', args)
 
        print(result_args[1])
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
if __name__ == '__main__':
    call_find_by_isbn()
	

The  find_by_isbn() stored procedure requires two parameters therefore we have to pass a list 
( args ) that contains two elements: the first one is isbn (1236400967773) and the second is 0. 
The second element of the args list (0) is just a placeholder to hold the  p_title parameter.

The  callproc() method returns a list ( result_args ) that contains two elements: the second 
element (result_args[1]) holds the value of the  p_title parameter.
