#zip.py

Basically, .zip is a container itself. It holds the real file inside. 
Similarly, Python zip is a container that holds real data inside. 
Python zip function takes iterable elements as input, and returns iterator.
======================================
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 
# using zip() to map values 
mapped = zip(name, roll_no, marks) 
# converting values to print as set 
mapped = set(mapped) 
# printing resultant values  
print ("The zipped result is : ",end="") 
print (mapped)
#The zipped result is : {('Shambhavi', 3, 60), ('Astha', 2, 70),
#('Manjeet', 4, 40), ('Nikhil', 1, 50)}
======================================
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 
mapped = zip(name, roll_no, marks) 
mapped = list(mapped) 
print ("The zipped result is : ",end="") 
print (mapped) 
print("\n") 
namz, roll_noz, marksz = zip(*mapped) 
print ("The unzipped result: \n",end="") 
print ("The name list is : ",end="") 
print (namz) 
print ("The roll_no list is : ",end="") 
print (roll_noz) 
print ("The marks list is : ",end="") 
print (marksz)

#The zipped result is : [('Manjeet', 4, 40), ('Nikhil', 1, 50), 
#('Shambhavi', 3, 60), ('Astha', 2, 70)]
#The unzipped result: 
#The name list is : ('Manjeet', 'Nikhil', 'Shambhavi', 'Astha')
#The roll_no list is : (4, 1, 3, 2)
#The marks list is : (40, 50, 60, 70)

==================================================
players = [ "Sachin", "Sehwag", "Gambhir", "Dravid", "Raina" ] 
scores = [100, 15, 17, 28, 43 ] 
for pl, sc in zip(players, scores): 
    print ("Player :  %s     Score : %d" %(pl, sc)) 

#Player :  Sachin     Score : 100
#Player :  Sehwag     Score : 15
#Player :  Gambhir     Score : 17
#Player :  Dravid     Score : 28
#Player :  Raina     Score : 43	
===================================================
test = zip()
# referring a zip class
print('The type of an empty zip : ', type(test))
list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six']
test = zip(list1, list2)  # zip the values
print('\nPrinting the values of zip')
for values in test:
    print(values)
#The type of an empty zip :  <class 'zip'>
#Print the values of zip
#('Alpha', 'one')
#('Beta', 'two')
#('Gamma', 'three')
#('Sigma', 'six')	
===========================================================
# list of 4 elements
list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
# list of 5 elements
list2 = ['one', 'two', 'three', 'six', 'five']
# list of 3 elments
list3 = [1, 2, 3]
test = zip(list1, list2, list3)  # zip the values
cnt = 0
print('\nPrinting the values of zip')
for values in test:
    print(values)  # print each tuples
    cnt+=1
print('Zip file contains ', cnt, 'elements.');	
#Printing the values of zip
#('Alpha', 'one', 1)
#('Beta', 'two', 2)
#('Gamma', 'three', 3)
#Zip file contains  3 elements.	
==============================================================
list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six']
test = zip(list1, list2)  # zip the values
testList = list(test)
a, b = zip( *testList )
print('The first list was ', list(a));
print('The second list was ', list(b));	
#The first list was  ['Alpha', 'Beta', 'Gamma', 'Sigma']
#The second list was  ['one', 'two', 'three', 'six']	
==============================================================
