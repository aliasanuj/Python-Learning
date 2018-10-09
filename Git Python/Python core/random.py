#random.py
====================================
import random
for x in range(1,10):
  print(random.randint(1,10),end = " ")
#6 7 2 4 2 1 6 10 10    
=============================
import random
for x in range(10):
  print(random.randint(1,21)*5, end=" ")
#90 5 80 60 10 65 40 90 45 30    
==============================
from random import random
print(random(),random(),random())
#0.0932117533793988 0.9908528802334776 0.28723843834999974
==============================
import random
list1 = [1,2,3,4,5]
print(random.choice(list1))
#any random no from list
=================================
import random
print(random.randrange(10,20))
#any no btwn 10-20
=================================
import random
print(random.randrange(10,21,5))
#10 20 30 anything 
==================================
import random
list1 = [1,2,3,4,5,6]
print(list1)
random.shuffle(list1)
print(list1)
#[1, 2, 3, 4, 5, 6]
#[2, 3, 1, 5, 6, 4]
====================================
import random 
print ("A random number from list is : ",end="") 
print (random.choice([1, 4, 8, 10, 3])) 
print ("A random number from range is : ",end="") 
print (random.randrange(20, 50, 3)) 
#A random number from list is : 3
#A random number from range is : 44
=====================================
import random 
print ("A random number between 0 and 1 is : ", end="")
print (random.random()) 
random.seed(5) 
print ("The mapped random number with 5 is : ", end="")
print (random.random()) 
random.seed(7) 
print ("The mapped random number with 7 is : ", end="")
print (random.random()) 
random.seed(5) 
print ("The mapped random number with 5 is : ",end="") 
print (random.random()) 
random.seed(7) 
print ("The mapped random number with 7 is : ",end="") 
print (random.random()) 
#A random number between 0 and 1 is : 0.15722560918770145
#The mapped random number with 5 is : 0.6229016948897019
#The mapped random number with 7 is : 0.32383276483316237
#The mapped random number with 5 is : 0.6229016948897019
#The mapped random number with 7 is : 0.32383276483316237
=====================================
import random 
li = [1, 4, 5, 10, 2] 
print ("The list before shuffling is : ", end="") 
for i in range(0, len(li)): 
    print (li[i], end=" ") 
print("\r") 
random.shuffle(li) 
print ("The list after shuffling is : ", end="") 
for i in range(0, len(li)): 
    print (li[i], end=" ") 
print("\r") 
print ("The random floating point number between 5 and 10 is : ",end="") 
print (random.uniform(5,10)) 
#The list before shuffling is : 1 4 5 10 2 
#The list after shuffling is : 1 2 5 4 10 

#The random floating point number between 5 and 10 is : 7.789287637079827
============================================
