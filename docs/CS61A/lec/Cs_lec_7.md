**Tree Abstraction**
trees grow *upside-down*

There are two repeatedly used definitions of trees:
- Recursive description(wooden tree)
	- A **tree** has a root **label** and a list of **branches** 
	- Each branch is a **tree**
	- A tree with zero branches is called a **leaf**
- Relative description(family tree)
	- Each location in a tree is called a **node**
	- Each **node** has a label that can be any value
	- One node can be the parent/child of any other

**Implementing the tree abstraction:**
![[chrome_i3Melqbx2F.png]]
So the tree can be implemented however it is fit
```jupyter
#Example implementation
def tree(label, branches=[]):
	"""Construct a tree with the given label value and a list of branches."""

	if change_abstraction.changed:
		for branch in branches:
			assert is_tree(branch), 'branches must be trees'
		return {'label': label, 'branches': list(branches)}
	else:
		for branch in branches:
			assert is_tree(branch), 'branches must be trees'
		return [label] + list(branches)
treek = tree('mytree',[tree(3)])
```
All branches of any *tree* must be a *tree*
```Python
def is_leaf(tree):
	return not branches(tree)
```
![[chrome_WJhOkZyTrB.png]]

Trees:
- (**ROOT LABEL**) + **A list of branches**

Can implement *tree as a list*:
```HTML
tree = [labels, list<branches> = []]
<!--So basically a tree has a branches variable, that when not initialised, default to [] value-->
```

```jupyter
def fib_tree(n):
	if n<=1:
		return tree(n)
	else:
		left,right = fib_tree(n-2),fib_tree(n-1)
		return tree(label(left)+label(right), [left,right])
def count_leaves(t):
	if is_leaf(t):
		return 1
	else:
		return sum([count_leaves(b) for b in branches(t)])
```
Sum a list of lists -> You get one list with all the elemnts in all the lists.

```jupyter
def print_tree(t, indent=0):
	print('  ' * indent + str(label(t)))
	
	for b in branches(t):
		print_tree(b, indent + 1)
```
