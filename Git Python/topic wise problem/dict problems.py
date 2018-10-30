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

