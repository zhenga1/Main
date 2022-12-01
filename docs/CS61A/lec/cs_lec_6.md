Limitations on dictionaries
- Dictionaries are collections of objects identified by keys. 
- Must be one to one, as in one key must only identify one object. Two keys cannot be equal: Can be at most one value for a given key

The first restriction is tied to Python's underlying implementation of dictionaries
The second restriction is tied to the nature of keys. 
Dictionary comprehensions:
```html
{<key exp>: <value exp> for <name> in <iter expression> if <filter exp>}
Short version: {<key exp>:<value exp> for <name> in <iter expression> }
```

![[Zoom_Ao7cbuRKCG.png]]

**Example: Indexing**
P: Implement index, takes a sequence of *keys*, a sequence of *values* and two argument *match* function. It returns dictionary from *keys* to lists in which the list for a key k contains all *values v* for which *match(k,v)* is a true value.
```jupyter
def index(keys,values,match):
	>>>index[[7,9,11],range(30,50),lambda k,v:v%k==0)]
	return {k:[v for v in values if match(k,v)] for k in keys}

```

**Data Abstraction**
- Compound values, combine other values together
	- A date: a year, a month and a day
	- A geographic position: latitude and longitude
- Data abstraction lets us manipulate compound values as units
- Isolate two parts of program, thinking about how data are represented

![[Zoom_XodIAcBeoS 1.png]]
**Rational Numbers**
- Exat representation of fractions -> before decimal evaluation
- A pair of integers (can express any rational) $p/q$
- As soon as division occurs, exact representation lost
- Assume we can compose and decompose rational numbers:
	- Constructor: rational(n,d)

***Rational number arithmetic implementation***
```jupyter
def mul_rational(x,y):
	return rational(numer(x)*numer(y),
	denom(x)*denom(y))
def add_rational(x,y):
	nx,dx = numer(x),denom(x)
	ny,dy = numer(y),denom(y)
	return rational(nx*dy+ny*dx,dx*dy)
def print_rational(x):
	print(numer(x),'/',denom(x))
def rationals_are_equal(x,y):
	return numer(x)*denom(y) == numer(y)*denom(x)
```
*Simplest possible definiton of rational and other functions*
```jupyter 
def rational(x,y):
	return [x,y]
def numer(r):
	return r[0]
def denom(r):
	return r[1]
```
Above code works, however have not yet computed in *lowest terms*

FIX: New definition of *rational(x,y)*
```jupyter
from math import gcd
def rational(x,y):
	d = gcd(x,y)
	return [x//d,y//d]
>>>tenth = rational(1,10)
>>>two_fifths = rational(2,5)
>>>print_rational(add_rational(tenth,two_fifths))
1/2
>>>type
class('type')
>>>
```


![[chrome_fH42C9kviA.png]]

**What are Data, how to abstract data?**
- We need to guarantee that constructor and selector functions work together to specify the right behaviour
- Behaviour condition: If we construct rational number $x$ form numerator $n$ and denominator $d$, then we must have that $numer(x)/denom(x) = n/d$ 
- Data abstractions use selectors and constructors to define behaviour
- If the conditions for the behaviour of the abstraction is met, then we have the representation is valid.
	- One can recognise data abstraction by its behaviour
	
*New way to implement rational:*
```jupyter
def rational(n,d):
	def select(name):
		if name == 'n':
			return n
		elif name=='d':
			return d
	return select
def numer(x):
	return x('n')
def denom(x):
	return x('d')
```
