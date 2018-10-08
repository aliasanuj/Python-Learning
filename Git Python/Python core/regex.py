#regex.py
===============================
import re 
p = re.compile('[a-e]') 
print(p.findall("Aye, said Mr. Gibenson Stark"))
#['e', 'a', 'd', 'b', 'e', 'a']
=============================
import re 
# \d is equivalent to [0-9]. 
p = re.compile('\d') 
print(p.findall("I went to him at 11 A.M. on 4th July 1886")) 
# \d+ will match a group on [0-9], group of one or greater size 
p = re.compile('\d+') 
print(p.findall("I went to him at 11 A.M. on 4th July 1886")) 
#['1', '1', '4', '1', '8', '8', '6']
#['11', '4', '1886']
=============================
import re 
# \w is equivalent to [a-zA-Z0-9_]. 
p = re.compile('\w') 
print(p.findall("He said * in some_lang.")) 
# \w+ matches to group of alphanumeric charcter. 
p = re.compile('\w+') 
print(p.findall("I went to him at 11 A.M., he said *** in some_language.")) 
# \W matches to non alphanumeric characters. 
p = re.compile('\W') 
print(p.findall("he said *** in some_language.")) 
#['H', 'e', 's', 'a', 'i', 'd', 'i', 'n', 's', 'o', 'm', 'e', '_', 'l', 'a', 'n', 'g']
#['I', 'went', 'to', 'him', 'at', '11', 'A', 'M', 'he', 'said', 'in', 'some_language']
#[' ', ' ', '*', '*', '*', ' ', ' ', '.']
===============================
import re 
# '*' replaces the no. of occurrence of a character. 
p = re.compile('ab*') 
print(p.findall("ababbaabbb"))
#['ab', 'abb', 'a', 'abbb']
================================
from re import split 
# '\W+' denotes Non-Alphanumeric Characters or group of characters 
# Upon finding ',' or whitespace ' ', the split(), splits the string from that point 
print(split('\W+', 'Words, words , Words')) 
print(split('\W+', "Word's words Words")) 
# Here ':', ' ' ,',' are not AlphaNumeric thus, the point where splitting occurs 
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM')) 
# '\d+' denotes Numeric Characters or group of characters 
# Spliting occurs at '12', '2016', '11', '02' only 
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM')) 
#['Words', 'words', 'Words']
#['Word', 's', 'words', 'Words']
#['On', '12th', 'Jan', '2016', 'at', '11', '02', 'AM']
#['On ', 'th Jan ', ', at ', ':', ' AM']
========================================
import re 
# Splitting will occurs only once, at '12', returned list will have length 2 
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 2)) 
# 'Boy' and 'boy' will be treated same when flags = re.IGNORECASE 
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags = re.IGNORECASE)) 
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here')) 
#['On ', 'th Jan 2016, at 11:02 AM']
#['On ', 'th Jan ', ', at 11:02 AM']
#['', 'y, ', 'oy oh ', 'oy, ', 'om', ' h', 'r', '']
#['A', 'y, Boy oh ', 'oy, ', 'om', ' h', 'r', '']
=========================================
import re 
# Regular Expression pattern 'ub' matches the string at "Subject" and "Uber". 
# As the CASE has been ignored, using Flag, 'ub' should match twice with the string 
# Upon matching, 'ub' is replaced by '~*' in "Subject", and in "Uber", 'Ub' is replaced. 
print(re.sub('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE)) 
# Consider the Case Senstivity, 'Ub' in "Uber", will not be reaplced. 
print(re.sub('ub', '~*' , 'Subject has Uber booked already')) 
# As count has been given value 1, the maximum times replacement occurs is 1 
print(re.sub('ub', '~*' , 'Subject has Uber booked already', count=1, flags = re.IGNORECASE)) 
# 'r' before the patter denotes RE, \s is for start and end of a String. 
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)) 
#S~*ject has ~*er booked already
#S~*ject has Uber booked already
#S~*ject has Uber booked already
#Baked Beans & Spam
==========================================
import re 
print(re.subn('ub', '~*' , 'Subject has Uber booked already')) 
t = re.subn('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE) 
print(t) 
print(len(t)) 
# This will give same output as sub() would have  
print(t[0])
#('S~*ject has Uber booked already', 1)
#('S~*ject has ~*er booked already', 2)
#2
#S~*ject has ~*er booked already
============================================
import re 
# escape() returns a string with BackSlash '\', before every Non-Alphanumeric Character 
# In 1st case only ' ', is not alphanumeric 
# In 2nd case, ' ', caret '^', '-', '[]', '\' are not alphanumeric 
print(re.escape("This is Awseome even 1 AM")) 
print(re.escape("I Asked what is this [a-9], he said \t ^WoW")) 
#This\ is\ Awseome\ even\ 1\ AM
#I\ Asked\ what\ is\ this\ \[a\-9\]\,\ he\ said\ \	\ \^WoW
============================================
import re 
  
# Lets use a regular expression to match a date string 
# in the form of Month name followed by day number 
regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "I was born on June 24") 
if match != None: 
  
    # We reach here when the expression "([a-zA-Z]+) (\d+)" 
    # matches the date string. 
  
    # This will print [14, 21), since it matches at index 14 
    # and ends at 21.  
    print ("Match at index %s, %s" % (match.start(), match.end())) 
  
    # We us group() method to get all the matches and 
    # captured groups. The groups contain the matched values. 
    # In particular: 
    #    match.group(0) always returns the fully matched string 
    #    match.group(1) match.group(2), ... return the capture 
    #    groups in order from left to right in the input string 
    #    match.group() is equivalent to match.group(0) 
  
    # So this will print "June 24" 
    print ("Full match: %s" % (match.group(0))) 
  
    # So this will print "June" 
    print ("Month: %s" % (match.group(1))) 
  
    # So this will print "24" 
    print("Day: %s" % (match.group(2)))
else: 
    print("The regex pattern does not match.")

#Match at index 14, 21
#Full match: June 24
#Month: June
#Day: 24
==================================
import re 
  
# a sample function that uses regular expressions 
# to find month and day of a date. 
def findMonthAndDate(string): 
      
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string) 
      
    if match == None:  
        print ("Not a valid date")
        return
  
    print ("Given Data: %s" % (match.group())) 
    print ("Month: %s" % (match.group(1))) 
    print ("Day: %s" % (match.group(2)))
  
      
# Driver Code 
findMonthAndDate("Jun 24") 
print("abc") 
findMonthAndDate("I was born on June 24") 
#Given Data: Jun 24
#Month: Jun
#Day: 24
#abc
#Not a valid date
==========================================
import re 
# A sample text string where regular expression  
# is searched. 
string  = """Hello my Number is 123456789 and 
             my friend's number is 987654321"""
# A sample regular expression to find digits. 
regex = '\d+'             
match = re.findall(regex, string) 
print(match)
#['123456789', '987654321']
===========================================
import re

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")
#matchObj.group() :  Cats are smarter than dogs
#matchObj.group(1) :  Cats
#matchObj.group(2) :  smarter
================================================
import re
phone = "2004-959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)
# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)
#Phone Num :  2004-959-559 
#Phone Num :  2004959559
=================================================================
https://www.tutorialspoint.com/python/python_reg_expressions.htm
==================================================================
