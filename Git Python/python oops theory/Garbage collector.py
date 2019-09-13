=============================================
============Python Garbage Collection========
=============================================
1. The process of memory management in Python is straightforward. 
Python handles its objects by keeping a count to the references each object have in the program, 
which means, each object stores how many times it is referenced in the program.
2. Garbage collection is the process of cleaning shared computer memory which is currently being put 
to use by a running program when that program no longer needs that memory. With Garbage collection, 
that chunk of memory is cleaned so that other programs (or same program) can use it again.
3. Garbage collection runs automatically as the program is under execution, sometimes, we might want to run 
the Garbage collection at a specific time. We can do this by calling collect() function.
4. If you want to manually manage the Garbage Collection in your application, 
start doing it only after the app has completely started and then continue doing so 
in steady operations.

Automatic garbage collection:
==============================
# loading gc 
import gc 
# get the current collection  
# thresholds as a tuple 
print("Garbage collection thresholds:", 
                    gc.get_threshold()) 
Output:
#Garbage collection thresholds: (700, 10, 10) 

Here, the default threshold on the above system is 700. This means when the number of allocations vs. 
the number of deallocations is greater than 700 the automatic garbage collector will run. 
Thus any portion of your code which frees up large blocks of memory is a good candidate for running 
manual garbage collection.

Manual Garbage Collection:
============================
Invoking the garbage collector manually during the execution of a program can be a good idea on how to 
handle memory being consumed by reference cycles.
The garbage collection can be invoked manually in the following way:

# Importing gc module 
import gc 
# Returns the number of 
# objects it has collected 
# and deallocated 
collected = gc.collect() 
# Prints Garbage collector  
# as 0 object 
print("Garbage collector: collected", 
          "%d objects." % collected) 

output :
#Garbage collector: collected 0 objects.

gc.enable()
Enable automatic garbage collection.

gc.disable()
Disable automatic garbage collection.

gc.isenabled()¶
Returns true if automatic collection is enabled.

gc.get_debug()
Return the debugging flags currently set.

gc.get_objects()
Returns a list of all objects tracked by the collector, excluding the list returned.
