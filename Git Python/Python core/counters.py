#counters.py
========================
#Counter --> It is container included in collection module.
#Container are object which hold objects.
#They provide a way to access the contained objects and iterable over them.
#Counter can be zero or negative also.
#Output --> Dict
#From collections import counter
==========================

from collections import Counter 
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red'] 
col_count = Counter(z) 
print(col_count) 
col = ['blue','red','yellow','green'] 
for color in col: 
    print (color, col_count[color]) 
#Counter({'blue': 3, 'red': 2, 'yellow': 1})
#blue 3
#red 2
#yellow 1
#green 0     
================================
from collections import Counter
string1 = "kumare anuj"
result1 = Counter(string1)
print(result1)
string2 = ["anuj","aman","anuj"]
result2 = Counter(string2)
print(result2)
#Counter({'u': 2, 'a': 2, 'k': 1, 'm': 1, 'r': 1, 'e': 1, ' ': 1, 'n': 1, 'j': 1})
#Counter({'anuj': 2, 'aman': 1})
=======================
from collections import Counter 
coun = Counter(a=1, b=2, c=3) 
print(coun) 
print(list(coun.elements())) 
#Counter({'c': 3, 'b': 2, 'a': 1})
#['a', 'b', 'b', 'c', 'c', 'c']
=======================
from collections import Counter 
coun = Counter(a=1, b=2, c=3, d=120, e=1, f=219) 
# This prints 3 most frequent characters 
for letter, count in coun.most_common(3): 
    print('%s: %d' % (letter, count)) 
#f: 219
#d: 120
#c: 3
==========================
from collections import Counter 
coun = Counter(a=1, b=2, c=3, d=120, e=1, f=219) 
# This prints 3 most frequent characters 
for i in coun.most_common(3): 
    print(i) 

#('f', 219)
#3('d', 120)
3('c', 3)
========================
from collections import Counter 
# With sequence of items  
print (Counter(['B','B','A','B','C','A','B','B','A','C'])) 
# with dictionary 
print (Counter({'A':3, 'B':5, 'C':2}))
# with keyword arguments 
print (Counter(A=3, B=5, C=2))
#Counter({'B': 5, 'A': 3, 'C': 2})
#Counter({'B': 5, 'A': 3, 'C': 2})
#Counter({'B': 5, 'A': 3, 'C': 2})
===========================
from collections import Counter 
coun = Counter() 
coun.update([1, 2, 3, 1, 2, 1, 1, 2]) 
print(coun) 
coun.update([1, 2, 4]) 
print(coun)
#Counter({1: 4, 2: 3, 3: 1})
#Counter({1: 5, 2: 4, 3: 1, 4: 1})
=============================
from collections import Counter 
c1 = Counter(A=4,  B=3, C=10) 
c2 = Counter(A=10, B=3, C=4) 
c1.subtract(c2) 
print(c1)
#Counter({'C': 6, 'B': 0, 'A': -6})
=============================
from collections import Counter 
# Create a list 
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red'] 
# Count distinct elements and print Counter aboject 
print(Counter(z))
#Counter({'blue': 3, 'red': 2, 'yellow': 1})
==============================
import collections
print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a':2, 'b':3, 'c':1}))
print(collections.Counter(a=2, b=3, c=1))
#Counter({'b': 3, 'a': 2, 'c': 1})
#Counter({'b': 3, 'a': 2, 'c': 1})
#Counter({'b': 3, 'a': 2, 'c': 1})
==============================
import collections
c = collections.Counter()
print('Initial :', c)
c.update('abcdaab')
print('Sequence:', c)
c.update({'a':1, 'd':5})
print('Dict    :', c)
#Initial : Counter()
#Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
#Dict    : Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})
================================
import collections
c = collections.Counter('abcdaab')
for letter in 'abcde':
    print('%s : %d' % (letter, c[letter]))
#a : 3
#b : 2
#c : 1
#d : 1
#e : 0
================================
import collections
c = collections.Counter('extremely')
c['z'] = 0
print(c)
print(list(c.elements()))
#Counter({'e': 3, 'x': 1, 't': 1, 'r': 1, 'm': 1, 'l': 1, 'y': 1, 'z': 0})
#['e', 'e', 'e', 'x', 't', 'r', 'm', 'l', 'y']
=====================================
import collections
c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')
print('C1:', c1)
print('C2:', c2)
print('\nCombined counts:')
print(c1 + c2)
print('\nSubtraction:')
print(c1 - c2)
print('\nIntersection (taking positive minimums):')
print(c1 & c2)
print('\nUnion (taking maximums):')
print(c1 | c2)
#C1: Counter({'b': 3, 'a': 2, 'c': 1})
#C2: Counter({'a': 2, 'l': 1, 'p': 1, 'h': 1, 'b': 1, 'e': 1, 't': 1})
#Combined counts:
#Counter({'a': 4, 'b': 4, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})
#Subtraction:
#Counter({'b': 2, 'c': 1})
#Intersection (taking positive minimums):
#Counter({'a': 2, 'b': 1})
#Union (taking maximums):
#Counter({'b': 3, 'a': 2, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})
============================================
from collections import Counter 
c = Counter(['eggs', 'ham'])
print(c['bacon'])
#0
=============================================
from collections import Counter 
c = Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))
#['a', 'a', 'a', 'a', 'b', 'b']
==============================================
from collections import Counter 
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)
#Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
==============================================
from collections import Counter 
a = "anuj"
b = "anju"
if Counter(a) == Counter(b):
  print("matched")
else :
  print("not matched")
#matched
===============================================
from collections import Counter
string1 = "kumare anuj"
result1 = Counter(string1)
print(result1)
string2 = ["anuj","aman","anuj"]
result2 = Counter(string2)
print(result2)
#Counter({'u': 2, 'a': 2, 'k': 1, 'm': 1, 'r': 1, 'e': 1, ' ': 1, #'n': 1, 'j': 1})
#Counter({'anuj': 2, 'aman': 1})
==================================================
from collections import Counter 
coun = Counter() 
coun.update([1, 2, 3, 1, 2, 1, 1, 2]) 
print(coun) 
coun.update([1, 2, 4]) 
print(coun)
#Counter({1: 4, 2: 3, 3: 1})
#Counter({1: 5, 2: 4, 3: 1, 4: 1})
==================================================
import collections
c = collections.Counter()
print('Initial :', c)
c.update('abcdaab')
print('Sequence:', c)
c.update({'a':1, 'd':5})
print(c)
#Initial : Counter()
#Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
#Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})
=======================================================
import collections
c = collections.Counter('abcdaab')
for letter in 'abcdefgh':
    print('%s : %d' % (letter, c[letter]))
#a : 3
#b : 2
#c : 1
#d : 1
#e : 0
#f : 0
#g : 0
#h : 0
=======================================================
