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
Letâ€™s examine at each method in more detail.

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


2. Insert multiple rows into a table

MySQL INSERT statement allows you to insert multiple rows by using  VALUES syntax. You just need to include 
multiple lists of column values. Each list is enclosed within parentheses and separated by commas. 
For example, to insert multiple books into the  books table, you use the following statement:

INSERT INTO books(title,isbn)
VALUES('Harry Potter And The Order Of The Phoenix', '9780439358071'),
       ('Gone with the Wind', '9780446675536'),
       ('Pride and Prejudice (Modern Library Classics)', '9780679783268');

To insert multiple rows into a table in Python, you use the  executemany() method of the MySQLCursor object. 
See the following code:


5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def insert_books(books):
    query = "INSERT INTO books(title,isbn) " \
            "VALUES(%s,%s)"
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.executemany(query, books)
 
        conn.commit()
    except Error as e:
        print('Error:', e)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
    books = [('Harry Potter And The Order Of The Phoenix', '9780439358071'),
             ('Gone with the Wind', '9780446675536'),
             ('Pride and Prejudice (Modern Library Classics)', '9780679783268')]
    insert_books(books)
 
if __name__ == '__main__':
    main()
	
- The logic in this example is similar to the logic in the first example. However, in this example, 
instead of calling the  execute() method, we use  executemany() method.
- In the  main() function, we pass a list of tuples, each contains title and isbn of the book.
- By calling the  executemany() method of the MySQLCursor object, the MySQL Connector/Python translates 
the  INSERT statement into the one that contains multiple lists of values.
- In this tutorial, we have shown you how to insert one or multiple rows into a MySQL table in Python.

