##########################################
#dictionary operations########################
##########################################

#Python Program to Add a Key-Value Pair to the Dictionary
key=int(input("Enter the key (int) to be added:"))
value=int(input("Enter the value for the key to be added:"))
d={}
d.update({key:value})
print("Updated dictionary is:")
print(d)

#Python Program to Concatenate Two Dictionaries Into One
d1={'A':1,'B':2}
d2={'C':3}
d1.update(d2)
print("Concatenated dictionary is:")
print(d1)

#Python Program to Check if a Given Key Exists in a Dictionary or Not
d={'A':1,'B':2,'C':3}
key=str(input("Enter key to check:"))
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")  ##case sensitive 
	  

	  
#Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)

#Python Program to Sum All the Items in a Dictionary
d={'A':100,'B':540,'C':239}
print("Total sum of values in the dictionary:")
print(sum(d.values()))
print(d.values())

##########################################
#dictionary operations########################
##########################################

#Python Program to Add a Key-Value Pair to the Dictionary
key=int(input("Enter the key (int) to be added:"))
value=int(input("Enter the value for the key to be added:"))
d={}
d.update({key:value})
print("Updated dictionary is:")
print(d)

#Python Program to Concatenate Two Dictionaries Into One
d1={'A':1,'B':2}
d2={'C':3}
d1.update(d2)
print("Concatenated dictionary is:")
print(d1)

#Python Program to Check if a Given Key Exists in a Dictionary or Not
d={'A':1,'B':2,'C':3}
key=str(input("Enter key to check:"))
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")  ##case sensitive 
	  

	  
#Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)

#Python Program to Sum All the Items in a Dictionary
d={'A':100,'B':540,'C':239}
print("Total sum of values in the dictionary:")
print(sum(d.values()))
print(d.values())

#Python Program to Multiply All the Items in a Dictionary
d={'A':10,'B':10,'C':239}
tot=1
for i in d:    
    tot=tot*d[i]
print(tot)

#Python Program to Remove the Given Key from a Dictionary
d = {'a':1,'b':2,'c':3,'d':4}
print("Initial dictionary")
print(d)
key=str(input("Enter the key to delete(a-d):"))
if key in d: 
    del d[key]
else:
    print("Key not found!")
    exit(0)
print("Updated dictionary")
print(d)

Initial dictionary
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
Enter the key to delete(a-d): c
Updated dictionary
{'a': 1, 'b': 2, 'd': 4}

#Python Program to Form a Dictionary from an Object of a Class
class A(object):  
     def __init__(self):  
         self.A=1  
         self.B=2  
obj=A()  
print(obj.__dict__)

{'A': 1, 'B': 2}


#Python Program to Map Two Lists into a Dictionary
list1 = ['a','b','c','d','e','f']
list2 = [1,2,3,4,5]
print(dict(zip(list1,list2)))

{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


keys=[]
values=[]
n=int(input("Enter number of elements for dictionary:"))
print("For keys:")
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    keys.append(element)
print("For values:")
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    values.append(element)
d=dict(zip(keys,values))
print("The dictionary is:")
print(d)

Enter number of elements for dictionary:1
For keys:
Enter element1:2
For values:
Enter element1:5
The dictionary is:
{2: 5}

#Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
test_string=str(input("Enter string:"))
l=[]
l=test_string.split()
l2 = []
for i in range(1,len(l)+1):
    l2.append(i)
print(dict(zip(l,l2)))

Enter string:apple nokia oneplus
{'apple': 1, 'nokia': 2, 'oneplus': 3}


#Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character

test_string=str(input("Enter string:"))
l=test_string.split()
d={}
for word in l:
    if(word[0] not in d.keys()):
        d[word[0]]=[]
        d[word[0]].append(word)
    else:
        if(word not in d[word[0]]):
          d[word[0]].append(word)
for k,v in d.items():
        print(k,":",v)
		
Enter string: apple nokia poco oppo oneplus
a : ['apple']
n : ['nokia']
p : ['poco']
o : ['oppo', 'oneplus']
