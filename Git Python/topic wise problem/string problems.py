##########################################
#String operations########################
##########################################

#Python Program to Replace all Occurrences of ‘a’ with $ in a String
string=str(input(("Enter string:")))
string=string.replace('a','$')
string=string.replace('A','$')
print("Modified string:")
print(string)

#Python Program to Remove the nth Index Character from a Non-Empty String
def remove(string, n):  
      first = string[:n]   
      last = string[n+1:]  
      return first + last
string=str(input(("Enter the sring:")))
n=int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(string, n))

Enter the sring: aanuja
Enter the index of the character to remove: 1
Modified string:
anuja

#Python Program to Detect if Two Strings are Anagrams
a1 = "kumaranuj"
a2 = "anujkumar"
b1 = sorted(a1)
print(b1)
b2 = sorted(a2)
print(b2)

['a', 'a', 'j', 'k', 'm', 'n', 'r', 'u', 'u']
['a', 'a', 'j', 'k', 'm', 'n', 'r', 'u', 'u']

s1=raw_input("Enter first string:")
s2=raw_input("Enter second string:")
if(sorted(s1)==sorted(s2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")
	  
#Python Program to Form a New String where the First Character and the Last Character have been Exchanged
def change(string):
      return string[-1:] + string[1:-1] + string[:1]
string=str(input(("Enter string:")))
print("Modified string:")
print(change(string))

Enter string: kumar anuj
Modified string:
jumar anuk

#Python Program to Count the Number of Vowels in a String
string=str(input("Enter string:"))
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)


n1 = str(input("enter the string :"))
n2 = []
v = ["a","e","i","o","u"]
for i in n1:
  if i in v:
    n2.append(i)
print("vowels are ",len(n2))


#Python Program to Take in a String and Replace Every Blank Space with Hyphen
n1 = str(input("enter the string :"))
x = n1.replace(" ","-")
print(x)

enter the string : my name is kumar anuj
my-name-is-kumar-anuj

#Python Program to Calculate the Length of a String Without Using a Library Function
string=str(input(("Enter string:")))
count=0
for i in string:
      count=count+1
print("Length of the string is:")
print(count)

#conversion sentance --> list --> sentances
n1 = str(input("Enter the sentence : "))
n2 = n1.split()
print(n2)
n3 = " ".join(n2)
print(n3)

Enter the sentence :  kumar anuj
['kumar', 'anuj']
kumar anuj

#Python Program to Remove the Characters of Odd Index Values in a String
def modify(string):  
  final = ""   
  for i in range(len(string)):  
    if i % 2 == 0:  
      final = final + string[i]  
  return final
string=str(input("Enter string:"))
print("Modified string is:")
print(modify(string))

Enter string: kumaranuj
Modified string is:
kmrnj

#Python Program to Calculate the Number of Words and the Number of Characters Present in a String
string=raw_input("Enter string:")
char=0
word=1
for i in string:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)

#larger string | smaller string
string1=str(input("Enter first string:"))
string2=str(input("Enter second string:"))
count1=0
count2=0
for i in string1:
      count1=count1+1
for j in string2:
      count2=count2+1
if(count1<count2):
      print("Larger string is:")
      print(string2)
elif(count1==count2):
      print("Both strings are equal.")
else:
      print("Larger string is:")
      print(string1)

Enter first string: kumar
Enter second string: anuj
Larger string is:
kumar

#Python Program to Count Number of Lowercase Characters in a String
string=str(input("Enter string:"))
count=0
for i in string:
      if(i.islower()):
            count=count+1
print("The number of lowercase characters is:")
print(count)

#Python Program to Count Number of Uppercase Characters in a String
string=str(input("Enter string:"))
count=0
for i in string:
      if(i.isupper()):
            count=count+1
print("The number of lowercase characters is:")
print(count)


#Python Program to Check if a String is a Palindrome or Not
string=str(input("Enter string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")

	  
#Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String
string=str(input("Enter string:"))
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)


#Python Program to Calculate the Number of Digits and Letters in a String
string=str(input("Enter string:"))
count1=0
count2=0
for i in string:
      if(i.isdigit()):
            count1=count1+1
      count2=count2+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)


#Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String=str(input("Enter string:"))
count=0
for i in string:
      count=count+1
new=string[0:2]+string[count-2:count]
print("Newly formed string is:")
print(new)


#Python Program to Count the Occurrences of Each Word in a Given String Sentence
n1=str(input("Enter string:"))
n2 = []
n3 = str(input("Enter string:"))
count=0
n2 = n1.split(" ")

for i in range(0,len(n2)):
  if n3 == n2[i]:
    count = count + 1
print(count)


#Python Program to Check if a Substring is Present in a Given String
string=str(input("Enter string:"))
sub_str=str(input("Enter word:"))
if(string.find(sub_str)==-1):
      print("Substring not found in string!")
else:
      print("Substring in string!")
	  
string=str(input("Enter string:"))
sub_str=str(input("Enter word:"))
for i in range(0,len(string)):
  if sub_str in string:
    print("it is there")
    break
  else:
    print("not there")
    break