**Q1 Mutability WWPD**
10/5 Disc 06

```jupyter
x = [1,2,3]
x+=[4]
x = x+[4]
```
We see that x+=[4] does the same thing as 
```jupyter
x.extend([4])
```
But the below:
```
x = x+[4]
```
Creates a new list and instead just assigns it to x. 

- is and == 
	- == (equal value of list) -> checks if values of operands are equal. comparison operator
	- is -> checks if operand points to the same thing. identity operator
- copying lists
	- lis[:] creates a shallow copy of list, essentially just copying over the pointers to lists and other mutable elements contained within the outer list
- return value of .pop(i)

**Iterators** will continue to iterate through a list even if the list is being changed mid iteration
