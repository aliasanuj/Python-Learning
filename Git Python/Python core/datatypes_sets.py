#sets :
===========
#Sets in Python
#A Set is an unordered collection data type that is iterable, mutable, and 
#has no duplicate elements. Python’s set class represents the mathematical 
#notion of a set. The major advantage of using a set, as opposed to a list, 
#is that it has a highly optimized method for checking whether a specific 
#element is contained in the set. This is based on a data structure known as a hash table.
===================================
#Frozen Sets Frozen sets are immutable objects that only support 
#methods and operators that produce a result without a?ecting the 
#frozen set or sets to which they are applied.
===================================
1. set --> mutable
2. frozenset --> Immutable
===================================
# Same as {"a", "b","c"} 
normal_set = set(["a", "b","c"]) 
# Adding an element to normal set is fine 
normal_set.add("d") 
print("Normal Set") 
print(normal_set) 
# A frozen set 
frozen_set = frozenset(["e", "f", "g"]) 
print("Frozen Set") 
print(frozen_set) 
# Uncommenting below line would cause error as 
# we are trying to add element to a frozen set 
# frozen_set.add("h") 
Output:
#Normal Set
#set(['a', 'c', 'b', 'd'])
#Frozen Set
#frozenset(['e', 'g', 'f'])
========================================
normal_set = set(["a", "b","c"])
print(normal_set)
normal_set.add("d")
print(normal_set)
frozen_set = frozenset(["e", "f", "g"])
print(frozen_set)
frozen_set.add("z")
print(frozen_set)
{'c', 'a', 'b'}
{'c', 'd', 'a', 'b'}
frozenset({'g', 'f', 'e'})
#AttributeError: 'frozenset' object has no attribute 'add'
========================================
1. add(x) Method: Adds the item x to set if it is not already present in the set.
people = {"Jay", "Idrish", "Archil"}
people.add("Daxit") 
-> This will add Daxit in people set.
people = {"Jay", "Idrish", "Archil"}
people.add("Daxit")
print(people)
people.add("Daxit")
print(people)
#{'Jay', 'Archil', 'Idrish', 'Daxit'}
#{'Jay', 'Archil', 'Idrish', 'Daxit'}
===============================
2. union(s) Method: Returns a union of two set.Using the ‘|’ operator between
#2 sets is the same as writing set1.union(set2)
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
population = people.union(vampires)
OR
population = people|vampires
#Set population set will have components of both people and vampire

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
population = people.union(vampires)
print(population)
population1 = people|vampires
print(population1)
#{'Arjun', 'Idrish', 'Archil', 'Karan', 'Jay'}
#{'Arjun', 'Idrish', 'Archil', 'Karan', 'Jay'}
==============================
3. intersect(s) Method: Returns an intersection of two sets.The ‘&’ 
#operator comes can also be used in this case.
victims = people.intersection(vampires)
-> Set victims will contain the common element of people and vampire

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun","Jay"} #case sensitive 'j' will not work
population = people.intersection(vampires)
print(population)
population1 = people&vampires
print(population1)
#{'Jay'}
#{'Jay'}
=================================
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun","jay"} #case sensitive 'j' will not work
population = people.intersection(vampires)
print(population)
population1 = people&vampires
print(population1)
set()
set()
=================================
4. difference(s) Method: Returns a set containing all the elements of invoking
# set but not of the second set. We can use ‘-‘ operator here.
safe = people.difference(vampires)
OR
safe = people – vampires
#-> Set safe  will have all the elements that are in people but not vampire

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun","Jay"} #case sensitive 'j' will not work
population = people.difference(vampires)
print(population)
population1 = people-vampires
print(population1)
#{'Idrish', 'Archil'}
#{'Idrish', 'Archil'}
=================================
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun","Jay"} #case sensitive 'j' will not work
population = people.difference(vampires)
print(population)
population1 = people-vampires
print(population1)
# {'Archil', 'Idrish'}
# {'Archil', 'Idrish'}
====================================
5. clear() Method: Empties the whole set.
victims.clear()
-> Clears victim set
However there are two major pitfalls in Python sets:
The set doesn’t maintain elements in any particular order.
Only instances of immutable types can be added to a Python set.

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun","Jay"} #case sensitive 'j' will not work
population = people.clear()
print(population)
#None
============================================
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)
#{'grapes', 'apple', 'banana', 'cherry', 'orange', 'mango'}
============================================
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#3
============================================
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#{'cherry', 'apple'}
=============================================
thisset = {"apple", "banana", "cherry"}
thisset.remove("abc")
print(thisset)
#    thisset.remove("abc")
============================================
thisset = {"apple", "banana", "cherry"}
thisset.discard("aaa")
print(thisset)
#{'apple', 'cherry', 'banana'}
# if the items will not be there, it wont yhrow any error
==============================================
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# apple
# {'banana', 'cherry'}
=============================================
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
#NameError: name 'thisset' is not defined
=============================================
thisset = {"apple", "banana", "cherry"}
del thisset["apple"]
del thisset[0]
print(thisset)
#TypeError: 'set' object does not support item deletion
#TypeError: 'set' object does not support item deletion
============================================
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#{'c', 1, 2, 3, 'a', 'b'}
================================================
set1 = {"a", "b" , "c"}
set2 = {1, 2, "b"}
set3 = set1.union(set2)
print(set3)
#{1, 2, 'b', 'a', 'c'}
================================================
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
#{1, 2, 3, 'b', 'c', 'a'}
===============================================
Note: Both union() and update() will exclude any duplicate items.
===============================================
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#{'apple', 'banana', 'cherry'}
=================================================
Method	Description :

add()	                	  Adds an element to the set
clear()	               		Removes all the elements from the set
copy()	                	Returns a copy of the set
difference()	        	  Returns a set containing the difference between two or more sets
difference_update()	    	Removes the items in this set that are also included in another, specified set
discard()	            	  Remove the specified item
intersection()	        	Returns a set, that is the intersection of two other sets
intersection_update()		  Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	        	  Returns whether two sets have a intersection or not
issubset()	            	Returns whether another set contains this set or not
issuperset()	        	  Returns whether this set contains another set or not
pop()	                	  Removes an element from the set
remove()	            	  Removes the specified element
symmetric_difference()  	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                 	Return a set containing the union of sets
update()	              	Update the set with the union of this set and others
=================================
