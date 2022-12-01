#r/discussion
- Discussion notes: link

# Discussion 10 /17
```jupyter
print("Hello world i am cool")
```
We see that 
```jupyter
class Rational:
	def __init__(self,numerator,denominator):
		self.numerator = numerator
		self.denominator = denominator
	def __str__(self):
		return f'{self.numerator}/{self.denominator}'
	def __repr__(self):
		return 
```
review from last class

**Linked List**
Is either empty or a first value and the rest of the linked list
``link = Link(1,Link(2))``
link -> (first) (rest)->[ first rest]

What is ``Link.empty?``
	It's a class attribute equal to an empty tuple

What are the instance attributes?
	.first- a value like the label of a tree
	.rest - a linked list or Link.empty.
``Link.rest.first`` for example will refer to the instance  attribute. 

**Traversing Linked Lists**
(iteratively(use pointers))
```jupyter 
pointer = lnk
while lnk!=Link.empty
	pointer = pointer.rest
```
Note: always pay attention to *mutation* vs *creation*
*Mutation:* Changing the attrubtes of Link, such as changing what `Link.first` is 
*Creation:* Creating a new Linked List using the `Link()` constructor

![[Code_L9BdmkmSYS.png]]

**Linked list property**
- `Link.first` is a value
- `Link.rest` is pointed to another Linked List. This can be itself(in which case the Linked List is effectively an infinite loop of values) or it can be another linked list. 

***Infinite Loop of Linked List:***
![[chrome_VryKFI14GY.png]]

Essentially, **every Linked List** is just a pointer

There is a **big difference** between mutating an object and creating a new, mutated object:
Assuming a function has parameter  `t`, which is a tree:
`t = Tree(prod,t.branches)`
	Creating a new (local) instance `t`, nothing to do with the passed in parameter t
`t.label = prod`
	Manipulating the parameter `t` instance itself.
In this case, to manipulate (mutate) the object, we must do the second option. 






