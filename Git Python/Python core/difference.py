Differences :
  
========================
========================
Generator vs iterator :
========================
========================
1. In creating a python generator, we use a function. But in creating an iterator in python, we use the iter() and next() functions.
2. A generator in python makes use of the ‘yield’ keyword. A python iterator doesn’t.
3. Python generator saves the states of the local variables every time ‘yield’ pauses the loop in python. An iterator does not 
make use of local variables, all it needs is iterable to iterate on.
4. A generator may have any number of ‘yield’ statements.
5. You can implement your own iterator using a python class; a generator does not need a class in python.
6. To write a python generator, you can either use a Python function or a comprehension. But for an iterator, you must use the 
iter() and next() functions.
7. Generator in python let us write fast and compact code. This is an advantage over Python iterators. They are also simpler to 
code than do custom iterator.

====================================
====================================
itertools vs functools
====================================
====================================
import itertools -----> itertools.accumulate -- return list
import functools -----> functools.reduce -- return singleton value (not list)
