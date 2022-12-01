***slice*** is a function that creates a *slice* object. Makes list slicing easier
- *slice(start, end, step)* creates a slice object that starts slicing list or iterable from *start* to *end*, kind of like a range object, each time stepping by *step* amount of times.
Example:
```Python
a = ("a", "b", "c", "d", "e", "f", "g", "h")  
x = slice(3, 5)  
print(a[x])
>>>Execute
('d','e')
```

```Python
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])
>>>Execute
('a','d','g')
```
Its a pretty cool function