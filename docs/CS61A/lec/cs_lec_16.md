**Lists in Environment Diagram**
**Assume that before each example below we execute**
`s=[2,3]`
`t=[5,6]`

Operation: **Append** adds one element to the list
Example: 
`s.append(t)`
`t=0`
Result:
`s -> [2,3,[5,6]]`
`t->0`

Operation **Extend** combines list elements one after another
`a = [1,[2]]`
`b=[[3],4]`
`c = a+b`
`d=[a,b]`

Operation **addition and slicing** creates new lists containing existing elements
`a=s+[t]`
`b=a[1:]`
`a[1] = 9`
`b[1][1]=0`

The **list** function also creates a new list contianing existing elements
`t=list(s)`
`s[1] = 0`

`a = [1,[2],3]`
`b = list(a)`
So in this case we would have $b$ is $a$,
![[chrome_KJwaFV9XZz.png]]
![[chrome_jNdnZFw6Sg.png]]
**List in Lists in Lists in Environment Diagrams**
`t=[1,2,3]`
`t[1:3] = [t]`
`t.extend(t)`
So the above example will return:
`t=[1, [...], 1, [...]]`, where the $...$ basically represents $t$ nested within the original list t. 

`t = [[1,2],[3,4]]`
`t[0].append(t[1:2])`

![[WhatsApp Image 2022-10-21 at 1.43.02 PM.jpeg]]
![[WhatsApp Image 2022-10-21 at 1.45.55 PM.jpeg]]
`john.elf.work(john)` 
-> 'Peon, I work'

**Example: Iterables and Iterators**
**Using BUilt-in Functions and Comprehensions**
What are the indices of all elements in a list s that have the smallest absolute value?
```python
def min_abs_indices(s):
	min_abs = min(map(abs,s))
	return [i for i in range(len(s)) if s[i] == min_abs]
```
What's the largest sum of two adjacent elements in a list s? (Assume len(s) > 1)
```python
def sum_indices(s):
	return max([s[i]+s[i+1] for i in range(len(s)-1)])
```
Another method
```python
def sum_indices(s):
	return list(zip(s[0:len(s)-1],s[1:]))
```

Create a dictionary mapping each digit d to the lists of elements in s that end with d.
```python
def dic_comprehension(s):
	lis = [n%10 for i in s]
	return {i: [x for x in s if x%10==i] for i in range(10) if i in [n%10 for n in s]}
```

