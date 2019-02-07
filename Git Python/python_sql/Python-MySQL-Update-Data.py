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

















