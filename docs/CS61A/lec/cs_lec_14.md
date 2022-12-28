#r/lecture
- Lecture notes: link

# Lecture: 10/17
```jupyter
print("Hello world i am cool")
```

**Efficiency**
We have to call f on n.
```jupyter
def fib(n):
	"""The n'th fibonacci number.
	"""
	if n==0 or n==1:
		return n
	else:
		return fib(n-2) + fib(n-1)
def count(f):
	def counted(n):
		counted.call_count+=1
		return f(n)
	#Effectively creates an attribute of the function in counted.
	counted.call_count = 0
	return counted
```
![[Obsidian_wxZrzJYOAv.png]]

Memoization
---
**Idea**: Remember the results that have been computed before

```jupyter
def memo(f):
	cache = {}
	def memoized(f):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return memoized
```

We see that the tree:
Memoization is a cousin of dynamic programming, I suppose dynamic programming is just like from the bottom to the top?
![[chrome_qLr5GwZLtf.png]]

Exponentiation
--
**Goal:** one more multipliation lets us double the problem size.
![[chrome_S69zzFaDvM 1.png]]
```jupyter
def exp(b,n):
	if n==0:
		return 1
	else:
		return b*exp(b,n-1)
#Newer example
def exp(b,n):
	if n==0:
		return 1
	elif n%2==0:
		return (exp(b,n//2))**2
	else:
		return b*exp(b,n-1)
```

Time in the Jupyter notebook can be figured out by the ``%time`` call
For first example, the larger the n, the greater the time taken. It appears to be (in general) a linear trend. (Using jupyter time)

However, for the faster example, the trend is more logarithmic, and the (absolute value) of the time taken itself is much less. 

First Example(LINEAR TIME)
Second Example(LOGARITHMIC TIME)

We have that for the LINEAR TIME:
- Doubling the input **doubles** the time
- 1024x the input takes 1024x as much time

For the LOGARITHMIC TIME:
- Doubling the input **increases** the time by one step
- 1024x the input takes 10 more steps lol. 

==The description of how the functional computation time grows relative to the sizeof $n$ is called the **Orders of Growth**==

**Quadratic time**
Functions that process all pairs of values in a sequence of length $n$ takes quadratic time

```jupyter
def overlab(a,b):
	count=0
	for item in a:
		for other in b:
			if item==other:
				count+=1
	return count
```
`overlap([2,3,5,2],[4,3,5,2])`  is a function with `O(4^2)`

So time taken $T$ is related to $n$ by:
$T = an^2 + bn+c$,where $a$ is a nonzero constant

![[chrome_HBIdOtZFUb.png]]
**Common orders of growth**
![[chrome_FzaeK4fUUE.png]]

**Logarithmic growth:**
- Doubling n increments time by a constant

**Linear growth:**
- Incrementing n increases time by constant

**Quadratic growth:**
- Incrementing n increases time by n times a constant. 

**Exponential growth:**
- Incrementing n multiplies (existing) time by a constant. 

**Factorial growth:**
- Incrementing n multiplies (existing) time by $n+1$

![[chrome_gKJ2aGdrRh.png]]