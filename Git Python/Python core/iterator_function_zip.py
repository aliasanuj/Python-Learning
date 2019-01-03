#iterator_function_zip.py
============================
1. Iterator Functions --> This iterator take two argument.Iterator target and function which would be followed at each iteration
of value in target.
2. If no function will be pass,addition take place by default.If iterable will be empty, output iterable will be also empty.
3. Chain(iter1,iter2,....) --> used to print all values 
4. We need to import itertools
- itertools.accumulate(list1)
- itertools.chain(list4) #list1+list2+list = list4
- itertools.chain.from_iterable(list3) #list3=[list1,list2]
- itertools.dropwhile() --> This iterator start printing the characters only after the function in argument.Return false for first time.
- itertools.filterfalse(func,seq) --> As the name suggest, this iterator prints only values that return false for passed function.
- itertools.isslice(iterable,start,stop,step)
- itertools.starmap(function,tuplelist)
- itertools.starmap(max,list)
- itertools.starmap(min,list)
- itertools.takewhile(func,iterator)
- itertools.tee(func,iterable)
- itertools.product(iter1,iter2)
- itertools.permutation(iter1,group-size)
- itertools.combination(iter1,group-size)
- itertools.combination_with_replacement(iter1,group-size)
- itertools.count(start,stop)
- itertools.cycle(iterable)
- itertools.repeat(val,num)
=====================================
import itertools 
import operator 
li1 = [1, 4, 5, 7] 
li2 = [1, 6, 5, 9] 
li3 = [8, 10, 5, 4] 
print ("The sum after each iteration is : ",end="") 
print (list(itertools.accumulate(li1))) 
print ("The product after each iteration is : ",end="") 
print (list(itertools.accumulate(li1,operator.mul))) 
print ("All values in mentioned chain are : ",end="") 
print (list(itertools.chain(li1,li2,li3))) 
#The sum after each iteration is : [1, 5, 10, 17]
#The product after each iteration is : [1, 4, 20, 140]
#All values in mentioned chain are : [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]
==============================================
import itertools 
li1 = [1, 4, 5, 7] 
li2 = [1, 6, 5, 9] 
li3 = [8, 10, 5, 4] 
li4 = [li1, li2, li3] 
print ("All values in mentioned chain are : ",end="") 
print (list(itertools.chain.from_iterable(li4))) 
print ("The compressed values in string are : ",end="") 
print (list(itertools.compress('GEEKSFORGEEKS',[1,0,0,0,0,1,0,0,1,0,0,0,0]))) 
#All values in mentioned chain are : [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]
#The compressed values in string are : ['G', 'F', 'G']
===============================================
import itertools 
li = [2, 4, 5, 7, 8] 
print ("The values after condition returns false : ",end="") 
print (list(itertools.dropwhile(lambda x : x%2==0,li))) 
print ("The values that return false to function are : ",end="") 
print (list(itertools.filterfalse(lambda x : x%2==0,li))) 
#The values after condition returns false : [5, 7, 8]
#The values that return false to function are : [5, 7]
================================================
import itertools 
li = [2, 4, 5, 7, 8, 10, 20] 
li1 = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10 , 1) ] 
print ("The sliced list values are : ",end="") 
print (list(itertools.islice(li,1, 6, 2))) 
print ("The values acc. to function are : ",end="") 
print (list(itertools.starmap(min,li1))) 
#The sliced list values are : [4, 7, 10]
#The values acc. to function are : [1, 1, 4, 1]
================================================
import itertools 
li = [2, 4, 6, 7, 8, 10, 20] 
iti = iter(li) 
print ("The list values till 1st false value are : ",end="") 
print (list(itertools.takewhile(lambda x : x%2==0,li ))) 
it = itertools.tee(iti, 3) 
print ("The iterators are : ") 
for i in range (0,3): 
    print (list(it[i])) 
#The list values till 1st false value are : [2, 4, 6]
#The iterators are : 
#[2, 4, 6, 7, 8, 10, 20]
#[2, 4, 6, 7, 8, 10, 20]
#[2, 4, 6, 7, 8, 10, 20]
================================================
import itertools 
print ("The combined values of iterables is  : ") 
print (*(itertools.zip_longest('GesoGes','ekfrek',fillvalue='_' ))) 
#The combined values of iterables is  : 
#('G', 'e') ('e', 'k') ('s', 'f') ('o', 'r') ('G', 'e') ('e', 'k') ('s', '_')
=================================================
import itertools 
print ("The cartesian product of the containers is : ") 
print (list(itertools.product('AB','12'))) 
print ("All the permutations of the given container is : ") 
print (list(itertools.permutations('GfG',2))) 
#The cartesian product of the containers is : 
#[('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]
#All the permutations of the given container is : 
#[('G', 'f'), ('G', 'G'), ('f', 'G'), ('f', 'G'), ('G', 'G'), ('G', 'f')]
=================================================
import itertools 
print ("All the combination of container in sorted order(without replacement) is : ") 
print (list(itertools.combinations('1234',2))) 
print ("All the combination of container in sorted order(with replacement) is : ") 
print (list(itertools.combinations_with_replacement('GfG',2))) 
#All the combination of container in sorted order(without replacement) is : 
#[('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4'), ('3', '4')]
#All the combination of container in sorted order(with replacement) is : 
#[('G', 'G'), ('G', 'f'), ('G', 'G'), ('f', 'f'), ('f', 'G'), ('G', 'G')]
================================================
import itertools 
print ("Printing the numbers repeatedly : ") 
print (list(itertools.repeat(25,4)))
#Printing the numbers repeatedly : 
#[25, 25, 25, 25]
================================================
