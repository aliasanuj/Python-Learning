Differences :
  
------------------------>
Generator vs iterator :
------------------------>
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

------------------------>
itertools vs functools
------------------------>
import itertools : itertools.accumulate : return list
import functools : functools.reduce : return singleton value (not list)

------------------------>
#map vs filter
------------------------>
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
#[-5, -4, -3, -2, -1]
========================
number_list = range(-5, 5)
less_than_zero = list(map(lambda x: x < 0, number_list))
print(less_than_zero)
#[True, True, True, True, True, False, False, False, False, False]
=========================
1. Map applies a function to all the items in an input_list. Here is the blueprint:
2. map(function_to_apply, list_of_inputs)
=========================
1. As the name suggests, filter creates a list of elements for 
2. which a function returns true. Here is a short and concise example:
=========================
1. Reduce is a really useful function for performing some computation on a list and
returning the result. 
2. It applies a rolling computation to sequential pairs of values in a list. 
3. For example, if you wanted to compute the product of a list of integers.
4. So the normal way you might go about doing this task in python is using a basic for loop:
=========================
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
print(product)
#24
=============================
Now let’s try it with reduce:
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)
#24
=============================
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)
#24
==============================

