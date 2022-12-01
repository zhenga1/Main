#r/lecture
- Lecture notes: link

# Lecture: 10/3
```jupyter
print("Hello world i am cool")
```

HMWK 4 is out
**Iterators**
A container can provide an iterator that provides access to its elements in order
	iter(iterable): Return an iterator over the elements of an interable value
	next(iterator): Returns next element in iterator
	
```jupyter
>>>s = [3,4,5]
>>>t = iter(s)
>>>next(t)
3
```
So here its kinda like the first, the $t$ thingy, points to something. The first $next(t)$ will return the first element of the list. The following $next(t)$ will return the subsequent elements of the list, one by one.
```jupyter
>>>s = [[1,2],3,4,5]
>>>t = iter(s)
>>>next(s)
LIST not iterator
>>>s
[[1,2],3,4,5]
>>>
```
![[chrome_UeB89kZuGq.png]]

An **iterable value** is any value that can be passed to iter to produce an iterator 
![[chrome_F8TUN0xXED.png]]
Objects like lists, tuples, sets, dictionaries, strings, etc. are called iterables. In short and simpler terms, iterable is **anything that you can loop over**.

An **iterator** is returned from iter and can be passed to next; all iterators are mutable
[](![[chrome_c5xRMtsUoE.png]])

Example of errors:
![[pythonw_3fKNhKEPlv.png]]
We see that from this example, the (iterable value) that is passed into the iterator shouldn't change.

Can't change the order of a dictionary in python.

![[pythonw_taOCYuv6e4.png]]
However, above example shows that you can change the values within the dictionary (or iterable item that is being changed) freely, without causing an error.

**For statements**
Turns out you can go through the contents of a list using an interator using a for statement
![[pythonw_nwAb4iTf3O.png]]
So basically you can use an iterator with for statement, which will use up certain elements of the iterator (so if you for the iterator twice it wouldn't work), or u can direcly pass an iterable to for, which will auto create an iterator for the iterable.

# Built-in Iterator Functions
![[pythonw_oyE2FvM565.png]]
Just like the **int, list,string** functions, passing in an iterator into the **iter** function will just return the original iterator.

Iterator knows what it is iterating over and where the iterator itself is.

Many built-in Python sequence operations return iterators that compute results lazily
1) map(func,iterable): Iterate over func(x) for x in iterable
2) filter(func,iterable): Iterate over x in iterable if func(x)
3) zip(first_iter,second_iter): Iterate over co-indexed (x,y) pairs
4) reversed(sequence): Iterate over x in a sequence in reverse order

To view contents of iterator, place resulting elements in a container
- list(iterable). Create list containing all x in iterable
- tuple(iterable). Create tuple containing all x in iterable

![[pythonw_kz9UWCo26a.png]]

![[pythonw_lc9y9fwxPu.png]]
This shows what filter(x) exactly does, it filters certain elements of the iterator away that do not satisfy some mentioined condition. 

**The Zip Function**
The built-in **zip** function returns an iterator over co-indexed tuples.
![[chrome_rVNMgtOxtz.png]]


![[chrome_4h2mNCKqPN.png]]
Two distinct ways of writing a function **palindrome** that takes in a list **s** and returns whether the list is a palindrome or not.

**Reasons for using Iterators**
Code that processes an iterator (via next) or iterable(via for or iter) makes few assumptions about the data itself
- Changing the data representation from a **list** to a **tuple, map object** or **dict_keys** doesn't require rewriting code.

**Example: Casino Blackjack**
1) The dealing of the card can be dealt with by a list containing a random order of the cards being passed into the iter function
2) So then the dealing of the card uses the customised next() function for the dealer. 


