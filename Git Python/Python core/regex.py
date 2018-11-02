#regex.py
===========================
#A regular expression is a special sequence of characters that helps 
#you match or find other strings or sets of strings, using a specialized
#syntax held in a pattern. Regular expressions are widely used in UNIX world.
#The module re provides full support for Perl-like regular expressions in Python.
#The re module raises the exception re.error if an error occurs while compiling or using a regular expression.
#syntax : re.match(pattern, string, flags=0)
#pattern -->This is the regular expression to be matched.
#string -->This is the string, which would be searched to match the pattern at the beginning of string.
#flags -->You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.

#re.I -->Performs case-insensitive matching.
#re.L -->Interprets words according to the current locale. This interpretation affects the alphabetic group (\w and \W), as well as word boundary behavior(\b and \B).
#re.M -->Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).
#re.S -->Makes a period (dot) match any character, including a newline.
#re.U -->Interprets letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B.
#re.X -->Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker.

#^-->Matches beginning of line.
#$-->?Matches end of line.
#.-->?Matches any single character except newline. Using m option allows it to match newline as well.
#[...]-->?Matches any single character in brackets.
#[^...]-->?Matches any single character not in brackets
#re*-->Matches 0 or more occurrences of preceding expression.
#re+-->Matches 1 or more occurrence of preceding expression.
#re?-->Matches 0 or 1 occurrence of preceding expression.
#re{ n}-->?Matches exactly n number of occurrences of preceding expression.
#re{ n,}-->Matches n or more occurrences of preceding expression.
#re{ n, m} -->Matches at least n and at most m occurrences of preceding expression.
#a| b-->Matches either a or b.
#(re)-->Groups regular expressions and remembers matched text.
#(?imx)-->Temporarily toggles on i, m, or x options within a regular expression. If in parentheses, only that area is affected.
#(?-imx)-->Temporarily toggles off i, m, or x options within a regular expression. If in parentheses, only that area is affected.
#(?: re)-->Groups regular expressions without remembering matched text.
#(?imx: re)-->Temporarily toggles on i, m, or x options within parentheses.
#(?-imx: re)-->Temporarily toggles off i, m, or x options within parentheses.
#(?#...)-->Comment.
#(?= re)-->Specifies position using a pattern. Doesn't have a range.
#(?! re)-->Specifies position using pattern negation. Doesn't have a range.
#(?> re)-->Matches independent pattern without backtracking.
#\w-->Matches word characters.
#\W-->Matches nonword characters.
#\s-->Matches whitespace. Equivalent to [\t\n\r\f].
#\S-->Matches nonwhitespace.
#\d-->Matches digits. Equivalent to [0-9].
#\D-->Matches nondigits.
#\A-->Matches beginning of string.
#\Z-->Matches end of string. If a newline exists, it matches just before newline.
#\z-->Matches end of string.
#\G-->Matches point where last match finished.
#\b-->Matches word boundaries when outside brackets. Matches backspace (0x08) when inside brackets.
#\B-->Matches nonword boundaries.
#\n, \t, etc.-->Matches newlines, carriage returns, tabs, etc.
#\1...\9-->Matches nth grouped subexpression.
#\10-->Matches nth grouped subexpression if it matched already. Otherwise refers to the octal representation of a character code.

#character class
#[Pp]ython-->Match "Python" or "python"
#rub[ye]-->Match "ruby" or "rube"
#[aeiou]-->Match any one lowercase vowel
#[0-9]-->Match any digit; same as [0123456789]
#[a-z]-->Match any lowercase ASCII letter
#[A-Z]-->Match any uppercase ASCII letter
#[a-zA-Z0-9]-->Match any of the above
#[^aeiou]-->Match anything other than a lowercase vowel
#[^0-9]-->Match anything other than a digit

#.-->Match any character except newline
#\d-->Match a digit: [0-9]
#\D-->Match a nondigit: [^0-9]
#\s-->Match a whitespace character: [ \t\r\n\f]
#\S-->Match nonwhitespace: [^ \t\r\n\f]
#\w-->Match a single word character: [A-Za-z0-9_]
#\W-->Match a nonword character: [^A-Za-z0-9_]

# \w is equivalent to [a-zA-Z0-9_]. 
# \w+ matches to group of alphanumeric charcter. 
# \W matches to non alphanumeric characters. 
# '\W+' denotes Non-Alphanumeric Characters or group of characters 
#'\W+' denotes Non-Alphanumeric Characters or group of charactersUpon finding (,) or (') or whitespace ' ', the split(), splits the string from that point.

#re.match()
#re.search()
#re.findall()
#re.split()
#re.sub()
#re.compile()

#RE Module contacts
re.compile(pattern)
re.compile(pattern,string)
re.DEBUG()
re.LOCALE
re.MULTILINE
re.DOTALL
re.UNICODE
re.search
re.match
re.split
re.findall
re.finditer
re.sub
re.subn
re.escape
re.purge
re.error

#Regular expression objects
search
match
split
findall
finditer
sub
subn
flags
groups
groupindex
pattern

#Match expands
expands
group
groups
groupdict
start
end
span
pos
endpos
lastindex
lastgroup
re string 

===========================================
https://www.tutorialspoint.com/python/python_reg_expressions.htm
https://www.analyticsvidhya.com/blog/2015/06/regular-expression-python/
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
import re
string1 = '''anuj is 25 and Rupesh is 26
            Aman is 57 and anshu is 26'''
age = re.findall(r'\d{1,3}',string1)
name = re.findall(r'[A-Z][a-z]*',string1)
print(age)
print(name)
#['25', '26', '57', '26']
#['Rupesh', 'Aman']
================================
import re
string1 = '''anuj is 25 and Rupesh is 26
            Aman is 57 and anshu is 26'''
age = re.findall(r'\d{1,3}',string1)
name = re.findall(r'[A-Z][a-z]*',string1)
dict = {}
x = 0
for i in name:
    dict[i] = age[x]
    x = x+1
print(dict)
#{'Rupesh': '25', 'Aman': '26'}
===============================
import re
name = "anuj anuj Anuj aman Anuj"
regex = re.findall("Anuj",name)
for i in regex:
    print(i)
#Anuj
#Anuj
===============================
import re
string1 = "kumar anun Anuj"
if re.search("Anuj",string1):
    print("available")
else:
    print("not present")
#available
==============================
import re
name = "anuj anuj Anuj aman dhfjdAnujjghfd"
regex = re.findall("Anuj",name)
for i in regex:
    print(i)
#Anuj
#Anuj
==================================
import re
name = "anuj anuj Anuj aman dhfjdAnujjghfd"
regex = re.finditer("Anuj",name)
for i in regex:
    abc = i.span()
    print(abc)
#(10, 14)
#(25, 29)
=================================
import re
string = "sat pat nat mat"
regex = re.findall("[spne]at",string)
for i in regex:
    print(i)
#sat
#pat
#nat
===================================
import re
string ="sat pat nat mat"
regex = re.findall("[p-t]at",string)
for i in regex:
    print(i)
#sat
#pat
===================================
import re
string = "sat pat nat mat"
regex = re.findall("[^p-t]at",string)
for i in regex:
    print(i)
#nat
#mat
===================================
import re
string = "anuj anshu aman"
abc = re.compile("anuj")
string = abc.sub("aman",string)
print(string)
#aman anshu aman
==============================
import re
abc = "here is \\drogba"
print(re.search(r"\\drogba",abc))
#<re.Match object; span=(8, 15), match='\\drogba'>
==============================
import re
str = '''anuj
kumar
aman
anshu
'''
regex = re.compile("\n")
result = regex.sub(" ",str)
print(result)
#anuj kumar aman anshu 
==============================
import re
a = "12345649874044444"
print("matches:",len(re.findall("\d",a)))
print("matches:",len(re.findall("\D",a)))
print("matches:",len(re.findall("\d[4]",a)))
#matches: 17
#matches: 0
#matches: 6
==============================
import re
a = "12345 123456 1234567"
b = len(re.findall("\d{6,7}",a))
print(b)
#2
==============================
from re import split
# '\W+' denotes Non-Alphanumeric Characters or group of characters
# Upon finding (,) or (') or whitespace ' ', the split(), splits the string from that point
print(split('\W+', 'Words, words , Words'))
print(split('\W+', "Word's wo,rds Words"))
# Here ':', ' ' ,',' are not AlphaNumeric thus, the point where splitting occurs
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))
# '\d+' denotes Numeric Characters or group of characters
# Spliting occurs at '12', '2016', '11', '02' only
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))

#['Words', 'words', 'Words']
#['Word', 's', 'wo', 'rds', 'Words']
#['On', '12th', 'Jan', '2016', 'at', '11', '02', 'AM']
#['On ', 'th Jan ', ', at ', ':', ' AM']
