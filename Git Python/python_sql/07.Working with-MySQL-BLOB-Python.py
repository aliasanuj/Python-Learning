============================================================================
============================================================================
Working with-MySQL-BLOB-Python==============================================
http://www.mysqltutorial.org/python-mysql-blob/ ============================
============================================================================
This tutorial shows you how to work with MySQL BLOB data in Python, with examples 
of updating and reading BLOB data.

The  authors table has a column named  photo whose data type is BLOB. We will read data 
from a picture file and update to the photo column.

Updating BLOB data in Python :
First, we develop a function named  read_file() that reads a file and returns the 
file’s content:

def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo
	
Second, we create a new function named  update_blob() that updates photo for an author 
specified by author_id .

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def update_blob(author_id, filename):
    # read file
    data = read_file(filename)
 
    # prepare update query and data
    query = "UPDATE authors " \
            "SET photo = %s " \
            "WHERE id  = %s"
 
    args = (data, author_id)
 
    db_config = read_db_config()
 
    try:
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

1. First, we call the  read_file() function to read data from a file and return it.
2. Second, we compose an UPDATE statement that updates photo column for an author
specified by author_id . The  args variable is a tuple that contains file data 
and author_id . We will pass this variable to the  execute() method together 
with the query .
3. Third, inside the  try except block, we connect to the database, instantiate 
a cursor, and execute the query with args . To make the change effective, 
we call commit() method of the MySQLConnection object.
4. Fourth, we close the cursor and database connection in the  finally block.

Notice that we imported MySQLConnection and Error objects from the MySQL Connector/Python \
package and  read_db_config() function from the  python_mysql_dbconfig module that we developed in 
the previous tutorial.

Let’s test the  update_blob() function.

def main():
    update_blob(144, "pictures\garth_stein.jpg")
 
if __name__ == '__main__':
    main()
	
Inside the main function, we call the  update_blob() function to update the photo
column for the author with id 144. To verify the result, we select data from the 
authors table.

SELECT * FROM authors
WHERE id = 144;

id 		first_name		last_name		photo
144 	garth 			stein			BLOB

Reading BLOB data in Python :

In this example, we select BLOB data from the  authors table and write it into a file.
First, we develop a  write_file() function that write a binary data into a file as follows:

def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
		
Second, we create a new function named  read_blob() as below:

def read_blob(author_id, filename):
    # select photo column of a specific author
    query = "SELECT photo FROM authors WHERE id = %s"
 
    # read database configuration
    db_config = read_db_config()
 
    try:
        # query blob data form the authors table
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, (author_id,))
        photo = cursor.fetchone()[0]
 
        # write blob data into a file
        write_file(photo, filename)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
		

The  read_blob() function reads BLOB data from the  authors table and write it 
into a file specified by the  filename parameter.

- First, we compose a SELECT statement that retrieves photo of a specific author.
- Second, we get the database configuration by calling the  read_db_config() function.
- Third, inside the  try except block, we connect to the database, instantiate cursor, 
and execute the query. Once we got the BLOB data, we use the  write_file() function to 
write it into a file specified by the filename .
- Fourth, in the finally block, we close the cursor and database connection.

Now, let’s test the  read_blob() function.

def main():
    read_blob(144,"output\garth_stein.jpg")
 
if __name__ == '__main__':
    main()

If you open the output folder in the project and see a picture there, it means that you 
have successfully read the blob from the database.









