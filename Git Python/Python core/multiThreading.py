https://medium.com/contentsquare-engineering-blog/multithreading-vs-multiprocessing-in-python-ece023ad55a

#Its all about MultiThreading.py
===================================
1. A thread is an entity within a process that can be scheduled for execution.
2. Also, it is the smallest unit of processing that can be performed in an OS (Operating System).
3. In simple words, a thread is a sequence of such instructions within a program that can 
be executed independently of other code. For simplicity, you can assume that a 
thread is simply a subset of a process!
4. A thread contains all this information in a Thread Control Block (TCB)
Thread Identifier: Unique id (TID) is assigned to every new thread
===================================
Multithreading
1. Multiple threads can exist within one process where:
2. Each thread contains its own register set and local variables (stored in stack).
3. All thread of a process share global variables (stored in heap) and the program code.
4. Multithreading is defined as the ability of a processor to execute multiple threads concurrently.
=====================================
import threading
def print_cube(num):
    print("Cube: {}".format(num * num * num))
def print_square(num):
    print("Square: {}".format(num * num))
if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,)) #args=(10,) must be tuple
    t2 = threading.Thread(target=print_cube, args=(10,)) #args=(10,) must be tuple
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!")


#Square: 100
#Cube: 1000
#Done!
==================================
Let us try to understand the above code:
To import the threading module, we do:
import threading
To create a new thread, we create an object of Thread class. It takes following arguments:
target: the function to be executed by thread
args: the arguments to be passed to the target function
In above example, we created 2 threads with different target functions:
====================================
t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))
To start a thread, we use start method of Thread class.
t1.start()
t2.start()
Once the threads start, the current program (you can think of it 
like a main thread) also keeps on executing. In order to stop execution 
of current program until a thread is complete, we use join method.
t1.join()
t2.join()
As a result, the current program will first wait for the completion of 
t1 and then t2. Once, they are finished, the remaining statements 
of current program are executed.
==================================================
import threading 
import os 
  def task1(): 
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name)) 
    print("ID of process running task 1: {}".format(os.getpid())) 
  def task2(): 
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name)) 
    print("ID of process running task 2: {}".format(os.getpid())) 
  if __name__ == "__main__": 
  
    # print ID of current process 
    print("ID of process running main program: {}".format(os.getpid())) 
  
    # print name of main thread 
    print("Main thread name: {}".format(threading.main_thread().name)) 
  
    # creating threads 
    t1 = threading.Thread(target=task1, name='t1') 
    t2 = threading.Thread(target=task2, name='t2')   
  
    # starting threads 
    t1.start() 
    t2.start() 
  
    # wait until all threads finish 
    t1.join() 
    t2.join()
============================
ID of process running main program: 245
Main thread name: MainThread
Task 1 assigned to thread: t1
ID of process running task 1: 245
Task 2 assigned to thread: t2
ID of process running task 2: 245
================================
Let us try to understand the above code:
We use os.getpid() function to get ID of current process.
print("ID of process running main program: {}".format(os.getpid()))
As it is clear from the output, the process ID remains same for all threads.
We use threading.main_thread() function to get the main thread object. 
In normal conditions, the main thread is the thread from which the 
Python interpreter was started. name attribute of thread object is used to get the name of thread.
print("Main thread name: {}".format(threading.main_thread().name))
We use the threading.current_thread() function to get the current thread object.
print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
==============================
The Threading Module :
1. The newer threading module included with Python 2.4 provides much more powerful, 
high-level support for threads than the thread module discussed in the previous section.
2. The threading module exposes all the methods of the thread module and provides some additional methods −
==============================
threading.activeCount() − Returns the number of thread objects that are active.
threading.currentThread() − Returns the number of thread objects in the caller's thread control.
threading.enumerate() − Returns a list of all thread objects that are currently active.
==============================
In addition to the methods, the threading module has the Thread class that implements threading.
The methods provided by the Thread class are as follows −
1. run() − The run() method is the entry point for a thread.
2. start() − The start() method starts a thread by calling the run method.
3. join([time]) − The join() waits for threads to terminate.
4. isAlive() − The isAlive() method checks whether a thread is still executing.
5. getName() − The getName() method returns the name of a thread.
6. setName() − The setName() method sets the name of a thread.
==================================
Multithreaded Priority Queue :
The Queue module allows you to create a new queue object that can hold a specific number of items.
There are following methods to control the Queue −
1. get() − The get() removes and returns an item from the queue.
2. put() − The put adds item to a queue.
3. qsize() − The qsize() returns the number of items that are currently in the queue.
4. empty() − The empty( ) returns True if queue is empty; otherwise, False.
5. full() − the full() returns True if queue is full; otherwise, False.
==============================
import threading
def calc_square(number):
    print('Square:' , number * number)
def calc_quad(number):
    print('Quad:' , number * number * number * number)
if __name__ == "__main__":
    number = 7
thread1 = threading.Thread(target=calc_square, args=(number,))
thread2 = threading.Thread(target=calc_quad, args=(number,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
#Square: 49
#Quad: 2401
==================================
import multiprocessing
def calc_square(number):
    print('Square:' , number * number)
    result = number * number
    print(result)
def calc_quad(number):
    print('Quad:' , number * number * number * number)
if __name__ == "__main__":
    number = 7
    result = None
p1 = multiprocessing.Process(target=calc_square, args=(number,))
p2 = multiprocessing.Process(target=calc_quad, args=(number,))
p1.start()
p2.start()
p1.join()
p2.join()
print(result)
#Square: 49
#49
#Quad: 2401
#None
=====================================
import time
from threading import Thread
def sleepMe(i):
    print("Thread %i going to sleep for 5 seconds." % i)
    time.sleep(5)
    print("Thread %i is awake now." % i)
for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
Thread 0 going to sleep for 5 seconds.
Thread 1 going to sleep for 5 seconds.
Thread 2 going to sleep for 5 seconds.
Thread 3 going to sleep for 5 seconds.
Thread 4 going to sleep for 5 seconds.
Thread 5 going to sleep for 5 seconds.
Thread 6 going to sleep for 5 seconds.
Thread 7 going to sleep for 5 seconds.
Thread 8 going to sleep for 5 seconds.
Thread 9 going to sleep for 5 seconds.
Thread 0 is awake now.
Thread 1 is awake now.
Thread 4 is awake now.
Thread 5 is awake now.
Thread 6 is awake now.
Thread 7 is awake now.
Thread 8 is awake now.
Thread 9 is awake now.
Thread 2 is awake now.
Thread 3 is awake now.
================================
In software programming, a thread is the smallest unit of execution with the 
independent set of instructions. It is a part of the process and operates in 
the same context sharing program’s runnable resources like memory. A thread has
a starting point, an execution sequence, and a result. It has an instruction 
pointer that holds the current state of the thread and controls what executes next in what order.
==============================
Similarly, the ability of a process to execute multiple threads parallelly is 
called multithreading. Ideally, multithreading can significantly improve the
performance of any program.
=================================
threading.activeCount() − Returns the number of thread objects that are active.
threading.currentThread() − Returns the number of thread objects in the caller's thread control.
threading.enumerate() − Returns a list of all thread objects that are currently active.
============================
In addition to the methods, the threading module has the Thread class that implements threading.
The methods provided by the Thread class are as follows −
1. run() − The run() method is the entry point for a thread.
2. start() − The start() method starts a thread by calling the run method.
3. join([time]) − The join() waits for threads to terminate.
4. isAlive() − The isAlive() method checks whether a thread is still executing.
5. getName() − The getName() method returns the name of a thread.
6. setName() − The setName() method sets the name of a thread.
================================
Multithreaded Priority Queue :
The Queue module allows you to create a new queue object that can hold a specific number of items.
There are following methods to control the Queue −
1. get() − The get() removes and returns an item from the queue.
2. put() − The put adds item to a queue.
3. qsize() − The qsize() returns the number of items that are currently in the queue.
4. empty() − The empty( ) returns True if queue is empty; otherwise, False.
5. full() − the full() returns True if queue is full; otherwise, False.
============================
