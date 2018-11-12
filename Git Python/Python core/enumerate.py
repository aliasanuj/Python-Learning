#enumerate.py
==============================
#It is built in function that take input as an iterator, list etc and return a tuple containing index and data at that
#index in the iterator sequence.
#syntax : enumerate(iteracble,start=0)
#Iterable --> Any object that support iteration.
#Start --> the index value from which the counter is to be started by default it is 0
======================================
l1 = ["eat","sleep","repeat"] 
s1 = "geek"
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 
print("Return type:",type(obj1)) 
print(list(enumerate(l1))) 
print(list(enumerate(s1,2))) 
#Return type: <class 'enumerate'>
#[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
#[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]
========================
l1 = ["eat","sleep","repeat"] 
for ele in enumerate(l1): 
    print(ele)
for count,ele in enumerate(l1,100): 
    print (count,ele) 
for count,ele in enumerate(l1,100): 
    print (ele,count) 
#(0, 'eat')
#(1, 'sleep')
#(2, 'repeat')
#100 eat
#101 sleep
#102 repeat
#eat 100
#sleep 101
#repeat 102
==========================
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 10):
    print(c, value)
#10 apple
#11 banana
#12 grapes
#13 pear
=========================
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list
#[(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
=========================
l1 = ["eat","sleep","repeat"]
for ele in enumerate(l1,10): 
    print(ele)
	
#(10, 'eat')
#(11, 'sleep')
#(12, 'repeat')
===============================
grocery = ['bread', 'milk', 'butter']
for item in enumerate(grocery):
  print(item)
print('\n')
for count, item in enumerate(grocery):
  print(count, item)
print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)
#(0, 'bread')
#(1, 'milk')
#(2, 'butter')
#
#
#0 bread
#1 milk
#2 butter
#
#
#100 bread
#101 milk
#102 butter
===========================
grocery = ['bread', 'milk', 'butter']
for i,j in enumerate(grocery):
  print(i)
#0
#1
#2
=============================
grocery = ['bread', 'milk', 'butter']
for i,j in enumerate(grocery):
  print(j)
#bread
#milk
#butter
=============================
str1 = "kumar"
print(list(enumerate(str1,2)))
#[(2, 'k'), (3, 'u'), (4, 'm'), (5, 'a'), (6, 'r')]
=============================
list1 = ["aman","anuj","anshu"]
for x in enumerate(list1,5):
  print(x)
for x,y in enumerate(list1,10):
  print(x,y)
#(5, 'aman')
#(6, 'anuj')
#(7, 'anshu')
#10 aman
#11 anuj
#12 anshu
============================
x = ["apple","banana","cherry"]
print(list(enumerate(x)))
#[(0, 'apple'), (1, 'banana'), (2, 'cherry')]
==============================
