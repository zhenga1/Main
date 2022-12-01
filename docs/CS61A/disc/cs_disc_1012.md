#r/discussion
- Discussion notes: link

# Discussion 10/12
```jupyter
print("Hello world i am cool")
```
**Object-oriented programming(OOP)**
- is a programming paradigm that allows us to treat data as objects, like we do in real life.
- For example, consider the class **Student**. Each of you as individuals are **instances** of the class(since we are all students)

Example:
**Callahan** -> is an instance of professor
**elle** -> is an instance of Student class.
Student:
- name (instance var)
- Understanding (instance var)
- Professor name 
We can write, for example
callahan.assist(elle)

@classmethod

# Representation
There are two main ways to produce the "string" of an object in Python: `str()` and `repr()`. While the two are similar, they are used for different purposes.

`str()` is used to describe the object to the end user in a "Human-readable" form, while `repr()` can be thought of as a "Computer-readable" form mainly used for debugging and development.

When we define a class in Python, `__str__` and `__repr__` are both built-in methods for the class.

We can call those methods using the global built-in functions `str(obj)` or `repr(obj)` instead of dot notation, `obj.__repr__()` or `obj.__str__()`.

In addition, the `print()` function calls the `__str__` method of the object, while simply calling the object in interactive mode calls the `_repr__` method.
