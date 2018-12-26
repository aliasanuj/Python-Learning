#any_all.py
=====================
any
=====================
#Returns true if any of the items is True. 
#It returns False if empty or all are false.
#Any can be thought of as a sequence of OR operations on the provided iterables.
#It short circuit the execution i.e. stop the execution as soon as the result is known.
=============================
all
=============================
#Returns true if all of the items are True (or if the iterable is empty).
#All can be thought of as a sequence of AND operations on the provided iterables.
#It also short circuit the execution i.e. stop the execution as soon as the result is known.
=============================
#any
=============================
print (any([False, False, False, False])) 
print (any([False, True, False, False])) 
print (any([True, False, False, False])) 
print(any([]))
#False
#True
#True
#False
==========================================
#all
print (all([True, True, True, True])) 
print (all([False, True, True, False])) 
print (all([False, False, False])) 
print(all([]))
#True
#False
#False
#True
==========================================
l = [1, 3, 4, 0]
print(any(l))
l = [0, False] #0 --> False
print(any(l))
l = [0, False, 5]
print(any(l))
l = []
print(any(l))
#True
#False
#True
#False
===========================================
s = "This is good"
print(any(s))
# 0 is False
# '0' is True
s = '000'
print(any(s))
s = ''
print(any(s))
#True
#True
#False
#It takes key. It will false when key = 0(int) | False(Boolean)
============================================
d = {0: 'False'}
print(any(d))
d = {0: 'False', 1: 'True'}
print(any(d))
d = {0: 'False', False: 0}
print(any(d))
d = {}
print(any(d))
# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))
#False
#True
#False
#False
#True
===============================================
#The all() method returns True when all elements in the given iterable are true. If not, it returns False.
===============================================
# all values true
l = [1, 3, 4, 5]
print(all(l))
# all values false
l = [0, False]
print(all(l))
# one false value
l = [1, 3, 4, 0]
print(all(l))
# one true value
l = [0, False, 5]
print(all(l))
# empty iterable
l = []
print(all(l))
#True
#False
#False
#False
#True
=================================================
s = "This is good"
print(all(s))
# 0 is False
# '0' is True
s = '000'
print(all(s))
s = ''
print(all(s))
#True
#True
#True
===================================
s = {0: 'False', 1: 'False'}
print(all(s))
s = {1: 'True', 2: 'True'}
print(all(s))
s = {1: 'True', False: 0}
print(all(s))
s = {}
print(all(s))
# 0 is False
# '0' is True
s = {'0': 'True'}
print(all(s))
#False
#True
#False
#True
#True
===================================
s = " "
print(any(s))
s = ""
print(any(s))
#True
#False
==================================
 
