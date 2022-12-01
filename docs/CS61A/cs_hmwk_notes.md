## Arms-length recursion

Before we get started, a quick comment on recursion with tree data structures. Consider the following function.

```jupyter
def min_depth(t): 
"""A simple function to return the distance between t's root and its closest leaf""" 
	if is_leaf(t): 
		return 0 
	# Base case---the distance between a node and itself is zero 
	h = float('inf') 
	# Python's version of infinity 
	for b in branches(t): 
		if is_leaf(b): return 1 # !!! 
		h = min(h, 1 + min_depth(b)) 
	return h
```
Arms length recursion is present above. We see that the is_leaf(b) does something that should have been processed by the call to the recursive function.  

Although the above implementation would work, would be faster than the previous implementation, and would give the desired answer, it is not ideal as it is a redundant step. 