#r/discussion
- Discussion notes: link

# Discussion 10/3
```jupyter
print("Hello world i am cool")
```

Shallow copy:
```jupyter
1st2 = [10,9,8,7,["hi","bye"]]
copy2 = lst2[:]
```
This is the shallow version of copy, which would individually copy across all the elements of the list. However, the inner list will not be deeply copied over as the copied outer list *copy2* will still contain the inner list.

```jupyter
lst = [1,2,3,4]
# next(lst) -> STATEMENT WILL ERROR
list_iter = iter(lst)
print(next(list_iter))
print(next(list_iter))
print(next(iter(list_iter)))
list_iter2 = iter(lst)
```
next(lst) -> error, can only call next on iterators

for statements also move the iterator "market" until end of sequence

**Analogy:**
Iterables are like books, go through them page by page. iterators are like bookmarks.

Iterable uses:
- range -> it returns (definitely) an iterable
- map takes in iterable and func, returns an iterator over function applied to all elements
- filter takes in a function as first parameter and an iterable in the second parameter. It then iterates through iterable if the 

>function(element in iterable)

returns True

Removes first instance of (x)


**You can also iterate through a tuple**