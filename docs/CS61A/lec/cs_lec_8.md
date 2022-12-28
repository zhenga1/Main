**Mutability**
Recursion:

```jupyter
def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)
fact(5)
def fact_times(n,k):
	#Supposed to be equivalent to computing
	#k*n*(n-1)*(n-2)...*1
	if n==0:
		return k
	else:
		return fact_times(n-1,k*n)
fact_times(5,10)
```

***Recursion. Essentially two options:***
1) Compute the (product, result, whatever) while using recursion
2) Compute the (product, result, whatever) after the recursion is complete(i.e, after the base case is reached)
	1) More challenging
	2) This case is kinda like one  of the homework problem

```jupyter
def print_sums(t,path_sum):
	#ATTEMPT AT IMPLEMENTATION
	#Print sum of labels along path from root to each leaf.
	#>>>print_sums(haste,'')
	#>>>print_sums(tree(3,[tree(4),tree(5,[tree(6)])]))
	has
	hat
	he
	path_sum = path_sum + label(t)
	if is_leaf(t):
		print(path_sum)
	else:
		for branch in branches(t):
			print_sums(branch,path_sum)
#print_sums(haste,'')
print_sums(tree(3,[tree(4),tree(5,[tree(6)])]),0)
```


**Count Paths that have a Total Label Sum**

```jupyter
from trees import *
def count_paths(t,total):
	found = 0
	if label(t) == total:
		found = 1
	else:
		found = 0
	return found + sum([count_paths(b,total-label(t)) for b in branches(t)])
	
```


**MUTABILITY**

```jupyter
from datetime import date
today = date(2022,9,28)
freedom = date(2022,12,14)
str(freedom-today)
```


```jupyter
freedom-today
```


```jupyter
lis = [today.year,today.month,today.day,today.strftime('%A, %B %d')]
lis
```


```jupyter
x = type(today)
x
```

**sturftime()**
cool method from the *date* class that allows the date specified to being showed in some sorta very interesting form

**Objects**
- objects represent information
- They consist of data and behviour, bundled together to create abstractions
- Can represent things, but also properties.
- Type of object is called **class**, **classes** are first-class values in Python

***Object orientated programming***
- A metaphor for organizing large programs
- Special syntax that can improve composition of programs

In Python, and many other programming languages;
- All **objects** have **attributes**

**Strings** -> Sorted by ASCII Standard

American Standard Code for Information Interchange
*Representing Strings: the Unicode Standard*
- 137,994 characters in Unicode 12.1
- 150 scripts
- ...

```jupyter
from unicodedata import lookup
lookup('BABY')
#lookup('FOOD')
```

![[IMG_0721.jpg]]
![[IMG_0722 1.jpg]]

![[pythonw_jC1wgxRkZW.png]]

![[chrome_AAi0yxbfSz.png]]
**Dictionary:**
**Mutation Can happen within function call**
A function can change value of any ojbecct within its scope:
Example:
```jupyter
def mystery(s):
	s.pop()
	s.pop()
four = [1,2,3,4]
mystery(four)
```
How to not change the elements within the parameter list:
```jupyter
def mystery(s):
	s = list(s)
	print(s.pop()+s.pop())
four = [1,2,3,4]
mystery(four)
```
Changing a list(without even passing in the list as parameter):
```jupyter
def another_mystery():
	four.pop()
	four.pop()
four = [1,2,3,4]
another_mystery()
four
```

**Tuples** are immutable, you can't change its contents
```jupyter
s = (3,4,5,6)
#tuple()
(3,4)+(5,6) #NEW TUPLE IS CREATED ALWAYS
#s[0:2]
#s = (8,9)
#s = (10,11)
```
Benefits of using tuples
-> Passing it through a function can never change the inherent values of a tuple
**Tuples are immutable sequence**
![[chrome_O7wO0iLgii.png]]

To see how the tree is represented in the current schematic, one can access this file
[[tree_representation]]