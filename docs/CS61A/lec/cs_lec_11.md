#r/lecture
- Lecture notes: link

# Lecture: 10/5
```jupyter
print("Hello world i am cool")
```
**A note on Large Numbers**
- Maximum number of interations that python can run in 1 minute: $10^9$

**Staff Solutions**


**Generators and Generator Functions**
A *generator function* is a function that yields values instead of returning them

A *normal function* returns once; a generator function can yield multiple times 

A *generator* is an *iterator* created automatically by calling a generator function 

When a generator function is called, it returns a generator that iterates over its yields.

Example:
```jupyter
def evens(start,end):
	even = start+start%2
	while even < end:
		yield even
		even+=2
t = evens(4,100000)
t
```
So for example, in the above example,
next(t) will allow the programme to iterate over the yields. 

Any code can be put into the function evens. So essentially the yield can allow you to create **customised iterators**

Only one frame is created for the function call **evens**. The function execution stops when **yield** is called, but the function frame is never removed or deleted.

When you call **next**, then the thing will calculate the next yield

**Generator Functions can Yield from Iterables**
*A yield from* statement yields all values from an iterator or iterable.
![[chrome_qki2nacJye.png]]
All *yield functions* return *generator functions*, which essentially are able to generate stuff and can be treated like an iterable.

Example of using *yield* function at the same time with recursion. 
![[WhatsApp Image 2022-10-05 at 1.47.08 PM.jpeg]]

Is definitely possible to construct a recursive function that returns an iterator. Also can iterate through recursive iterator. 

**Yielding Partitions**
A partition of a positive integer $n$, using parts up to size $m$, is a way in which $n$ can be expressed as the sum of positive integer parts up to $m$ in increasing order. 
![[chrome_R87EoGDgbR.png]]
**This is Partitioning and then printing it as a string**
![[chrome_4nHYJzbpds.png]]
This is then doing the same thing with partitions except using the yield functionality.
![[chrome_VFWrePKATh.png]]



