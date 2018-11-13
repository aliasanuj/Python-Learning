#sets
=================

#sets
================================
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
#1. add(x) Method: Adds the item x to set if it is not already present in the set.
people = {"Jay", "Idrish", "Archil"}
people.add("Daxit") 
-> This will add Daxit in people set.

#2. union(s) Method: Returns a union of two set.Using the ‘|’ operator between
#2 sets is the same as writing set1.union(set2)
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
population = people.union(vampires)
OR
population = people|vampires
#Set population set will have components of both people and vampire

#3. intersect(s) Method: Returns an intersection of two sets.The ‘&’ 
#operator comes can also be used in this case.
victims = people.intersection(vampires)
-> Set victims will contain the common element of people and vampire

#4. difference(s) Method: Returns a set containing all the elements of invoking
# set but not of the second set. We can use ‘-‘ operator here.
safe = people.difference(vampires)
OR
safe = people – vampires
#-> Set safe  will have all the elements that are in people but not vampire

#4.5. clear() Method: Empties the whole set.
victims.clear()
-> Clears victim set
However there are two major pitfalls in Python sets:
The set doesn’t maintain elements in any particular order.
Only instances of immutable types can be added to a Python set.

============================================
Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others



