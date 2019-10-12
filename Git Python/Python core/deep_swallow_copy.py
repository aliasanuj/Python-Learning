#deep_swallowcopy.py
===============================
Copy --> Python defines a module which allows to deep copy or shallow copy mutable objkect using inbuilt functions present in 
the module copy. Assignment ststements in python do not copy objects, they create bindings between a target and an object.
For collections that are mutable or contain mutable items,a copy is sometimes needed so one can change one copy without changing the
color.

Deep Copy --> In case of deep copy, an object is copied in another object. It means any change made to copy of object,
do not reflect in the original object. In python it is implemented using "deep copy()" function.
We need to import copy 

shallow copy -->In this, references of object is copied in other object. 
It means that any change made to a copy of object do reflect in the original object.
In python, it is implemented by "copy()" function.
========================================================
import copy 
li1 = [1, 2, [3,5], 4] 
li2 = copy.deepcopy(li1) 
print ("The original elements before deep copying") 
for i in range(0,len(li1)): 
    print (li1[i],end=" ") 
print("\r") 
li2[2][0] = 7
print ("The new list of elements after deep copying ") 
for i in range(0,len( li1)): 
    print (li2[i],end=" ") 
print("\r") 
print ("The original elements after deep copying") 
for i in range(0,len( li1)): 
    print (li1[i],end=" ")
#The original elements before deep copying
#1 2 [3, 5] 4 
#The new list of elements after deep copying 
#1 2 [7, 5] 4 
#The original elements after deep copying
#1 2 [3, 5] 4  
=======================================
import copy 
li1 = [1, 2, [3,5], 4] 
li2 = copy.copy(li1) 
print ("The original elements before shallow copying") 
for i in range(0,len(li1)): 
    print (li1[i],end=" ") 
print("\r") 
li2[2][0] = 7
print ("The original elements after shallow copying") 
for i in range(0,len( li1)): 
    print (li1[i],end=" ") 
#The original elements before shallow copying
#1 2 [3, 5] 4 
#The original elements after shallow copying
#1 2 [7, 5] 4 
==========================================
import copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)
print("Old list:", old_list)
print("New list:", new_list)
#Old list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#New list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
===========================================
import copy
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
old_list.append([4, 4, 4])
print("Old list:", old_list)
print("New list:", new_list)
#Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
#New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
============================================
import copy
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
old_list[1][1] = 'AA'
print("Old list:", old_list)
print("New list:", new_list)
#Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
#New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
=============================================
import copy
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)
print("Old list:", old_list)
print("New list:", new_list)
#Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
#New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
===============================================
import copy
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)
old_list[1][0] = 'BB'
print("Old list:", old_list)
print("New list:", new_list)
#Old list: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
#New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
=================================================
import copy
list1 = [1,2,3,4,[5,8,7],7]
list2 = copy.deepcopy(list1)
print(list1)
print(list2)
list2[4][2]=10
print(list1)
print(list2)
#[1, 2, 3, 4, [5, 8, 7], 7]
#[1, 2, 3, 4, [5, 8, 7], 7]
#[1, 2, 3, 4, [5, 8, 7], 7]
#[1, 2, 3, 4, [5, 8, 10], 7]
=================================================
import copy
list1 = [1,2,3,4,[5,8,7],7]
list2 = copy.copy(list1)
print(list1)
print(list2)
list2[4][2]=10
print(list1)
print(list2)
#[1, 2, 3, 4, [5, 8, 7], 7]
#[1, 2, 3, 4, [5, 8, 7], 7]
#[1, 2, 3, 4, [5, 8, 10], 7]
#[1, 2, 3, 4, [5, 8, 10], 7]
==================================================
