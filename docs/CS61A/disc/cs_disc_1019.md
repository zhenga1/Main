#r/discussion
- Discussion notes: link

# Discussion 10 /19
```jupyter
print("Hello world i am so incredibly cool")
```

**Linked list mini-lec**
`ganodorf = Link('zelda', Link('link',Link('sheik',Link.empty)))`

To get the value 'sheik' from the Linked list, we can use the expression:
`ganondorf.rest.rest.first`

Similarly,
`ganondorf.rest.first` outputs `link`

Another version of **Tree** implementation using **Object** notation:
```python
class Tree: 
	def __init__(self, label, branches=[]): 
		for b in branches: 
			assert isinstance(b, Tree) 
		self.label = label 
		self.branches = branches 
	def is_leaf(self): 
		return not self.branches
```

# Efficiency Mini-lec
Consider: finding the square of a number $x$ (the calculation is $x\cdot x$ ) -> This is $O(1)$

Consider: finding the factorial of a number $x$ (the calculation is $x\cdot (x-1)\cdot (x-2)\cdot(x-3)\dots 1$ -> This is $O(n)$ since it is linear in complexity






