## Tree Data Abstraction Implementation

For your reference, we have provided our implementation of trees as a data abstraction.

```jupyter
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)
t = tree(1, [tree(2), tree(4)])
t
```
```jupyter
is_leaf(t[1:][1])
```
```jupyter
[label(b) for b in branches(t)]
```
```jupyter
branches(tree(5, [t, tree(3)]))[0][0]
```
```jupyter
branches(tree(5, [t, tree(3)]))
```