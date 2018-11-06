#Range vs xrange 
====================
#range() vs xrange() in Python

#range() and xrange() are two functions that could be used to 
#iterate a certain number of times in for loops in Python. 
#In Python 3, there is no xrange , but the range function behaves 
#like xrange in Python 2.If you want to write code that will run on 
#both Python 2 and Python 3, you should use range().

#range() – This returns a list of numbers created using range() function.
#xrange() – This function returns the generator object that can be used to 
#display numbers only by looping. Only particular range is displayed on demand 
#and hence called “lazy evaluation“.

#Both are implemented in different ways and have different characteristics associated with them.
#The points of comparisons are:
#Return Type
#Memory
#Operation Usage
#Speed

#Return Type :
range() returns – the list as return type.
xrange() returns – xrange() object.
# Python code to demonstrate range() vs xrange() 
# on  basis of return type 
# initializing a with range() 
a = range(1,10000) 
# initializing a with xrange() 
x = xrange(1,10000) 
# testing the type of a 
print ("The return type of range() is : ") 
print (type(a)) 
# testing the type of x 
print ("The return type of xrange() is : ") 
print (type(x)) 

#Memory:
#The variable storing the range created by range() takes more memory as 
#compared to variable storing the range using xrange().
#The basic reason for this is the return type of range() is
# list and xrange() is xrange() object.

#Operations usage
#As range() returns the list, all the operations that can be 
#applied on the list can be used on it. On the other hand, as 
#xrange() returns the xrange object, operations associated to list
# cannot be applied on them, hence a disadvantage.

#Speed :
#Because of the fact that xrange() evaluates only 
#the generator object containing only the values that are 
#required by lazy evaluation, therefore is faster in 
#implementation than range().

#For the most part, xrange and range are the exact same in terms 
#of functionality. They both provide a way to generate a list of 
#integers for you to use, however you please. The only difference 
#is that range returns a Python list object and xrange returns an xrange object

#range() and xrange() Functionality
#In terms of functionality both range() and xrange() functions generates integer numbers within given range.
#i.e range (1,5,1) will produce [1,2,3,4] and xrange(1,5,1)  will produce [1,2,3,4]
#so no difference in terms of functionality between range() and xrange().

#range() and xrange() return value
#range() creates a list i.e. range returns a Python list object, for example, 
#range (1,500,1) will create a python list of 499 integers in memory. remember, 
#range() generates all numbers at once.
#xrange() functions returns an xrange object that evaluates lazily. 
#that means xrange only stores the range arguments and generates the 
#numbers on demand. it doesn’t generate all numbers at once like range(). and 
#this object only supports indexing, iteration, and the len() function.
#on the other hand xrange() generates the numbers on demand. that means it produces number 
#one by one as for Loop moves to the next number. In every iteration of for loop, 
#it generates the next number and assigns it to the iterator variable of for loop.


#range() and xrange() return type
#-->range() return type is Python list.
#-->xrange()  function returns xrange object.

#as you know xrange doesn’t actually generate a static list at run-time like range does. 
#xrange() creates the values on demand as you need them using a technique called yielding.
#range() function produced all numbers instantaneously before the for loop started executing.
#The main problem with the original range() function is it uses a very large amount of memory 
#if you are producing a huge range of numbers

#xrange() function always produces the next number on the fly i.e. 
#only keeps one number in memory at a time to consume less memory.

#If you are dealing with a large range of numbers then I recommend you to use xrange()
# i.e. you should always favor xrange() over a range() if we want to generate the huge range of numbers.
#This is very helpful if your system has less memory like cell phones. 
#using xrange() you can prevent memory overflow errors.
#As xrange() resolves each number lazily, if you stop iteration early,
# you won’t waste time creating the whole list.

#Scenarios where we can use range() function in python :
#If you want to iterate over the list multiple times then I recommend you to use range().
# because xrange has to generate an integer object every time you access an index, this will be overhead.
#If you need to generate fewer numbers then go for range() function.
#range() returns the list, so you can use all list operations on it.
#On the other hand, you know xrange() returns the xrange object, so you can’t use all list operations on it.
#Compatibility of code – If you want to write code that will run on both Python 2 and Python 3,
# use range() as the xrange function is deprecated in Python 3.

