#filter_function.py
========================
1. The filter() method constructs an iterator from elements of an iterable for which a function returns true.
2. In simple words, the filter() method filters the given iterable with the help of a function 
that tests each element in the iterable to be true or not.
3. The syntax of filter() method is:
filter(function, iterable)
filter() Parameters
4. The filter() method takes two parameters:
function - function that tests if elements of an iterable returns true or false
5. If None, the function defaults to Identity function - which returns false if any elements are false
iterable - iterable which is to be filtered, could be sets, lists, tuples, or containers of any iterators
========================
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
#[-5, -4, -3, -2, -1]
===========================
number_list = range(-5, 5)
less_than_zero = list(map(lambda x: x < 0, number_list))
print(less_than_zero)
#[True, True, True, True, True, False, False, False, False, False]
================================
number_list = range(-5, 5)
less_than_zero = tuple(filter(lambda x: x < 0, number_list))
print(less_than_zero)
#(-5, -4, -3, -2, -1)

==========================
def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
filtered = filter(fun, sequence) 
print('The filtered letters are:') 
for s in filtered: 
    print(s) 
#e
#e
==========================
seq = [0, 1, 2, 3, 5, 8, 13] 
result = filter(lambda x: x % 2, seq) 
print(list(result)) 
result = filter(lambda x: x % 2 == 0, seq) 
print(list(result)) 
#[1, 3, 5, 13]
#[0, 2, 8]
===========================
randomList = [1, 'a', 0, False, True, '0']
filteredList = filter(None, randomList)
print('The filtered elements are:')
for element in filteredList:
    print(element)
#The filtered elements are:
#1
#a
#True
#0
==============================
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)
for x in adults:
  print(x)
#18
#24
#32
==============================
list1 = [1,2,3,6,5,4,7,8,9]
result = map(lambda x : x>5,list1)
print(list(result))
#[False, False, False, True, False, False, True, True, True]
==============================


