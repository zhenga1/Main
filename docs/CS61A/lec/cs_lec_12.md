#r/lecture
- Lecture notes: link

# Lecture: 10/7
```jupyter
print("Hello world i am cool")
```
**Mutable values **

![[WhatsApp Image 2022-10-07 at 1.18.23 PM.jpeg]]

![[pythonw_5kBuKRGa2t.png]]

**Object-oriented programming**
**A method for organizing programs**
- Data abstraction
- Bundling together information and related behaviour
**A metaphor for computation using distributed state**
- Each object has its own local state
- Each object also knows how to manage its own local state, based on method calls
- Method calls (can be thought of) as messages passed between objects
- Several objects may all be instances of a common type
- Different types may relate to each other.

**Specialised syntax and vocabulary to support this metaphor**
![[WhatsApp Image 2022-10-07 at 1.25.30 PM.jpeg]]
# Classes
A **class** describes the general behaviour of its instances
**Idea:** All bank accounts have a *balance* and an account *holder*; the *Account* class should add those attributes to each newly created instance.

```jupyter
>>>a = Account('John')
>>>a.holder
'John'
>>>a.balance
```

**Idea:** All bank accounts should have **withdraw** and **deposit** behaviours that all work in the same way.

```jupyter
>>>a.deposit(15)
15
>>>a.withdraw(10)
5
>>>a.balance
5
```

**Better Idea**: All bank accounts share a **withdraw** method and a **deposit** method

# The class Statement
```python
class name:
	suite
```
A *class statement* creates a new class and binds that class to name in the first frame of the current environment

Assignment and def statements in suite creates attributes of the class (not names in frames)

**Object Construction**
**Idea:** All bank accounts have a **balance** and an account **holder**; The **Account** class should add those attributes to each of its instances.

![[WhatsApp Image 2022-10-07 at 1.32.40 PM.jpeg]]

Q: Is init kinda setting up defaults?
A: Not rlly, its kinda like *setting up the object* to *prepare it to be used*. 

Can't write **def constructor**, must write **def _init_**

The **_init_** function is always called whenever the constructor is called.

**Object Identity**
Every object that is an instance of a user-defined class has a unique identity:
![[chrome_HX8HwQpibp.png]]

**Methods**
Methods are functions defined in the suite of a class statement
![[chrome_hlpwVyZaMp.png]]

**Invoking Methods**
All invoked methods have access to the objet via the self parameter, and so they can all access and manipulate the object's state

**Dot Expressions**
Objects receive messages via dot notation

Dot notation accesses attributes of the instance or its class $<expression>,<name>$

The $<expression>$ can be any valid Python Expression
The $<name>$ must be a simple name

![[chrome_bqWGMOpvCG.png]]
Above expression evaluates to the value of the attribute looked up by $<name>$ in the object that is the value of the $<expression>$

![[WhatsApp Image 2022-10-07 at 1.52.10 PM.jpeg]]

Can also assign methods to instance.
Assume we have that $a$ is an Account object
```python
Account.deposit(a, amount) #would work
a.deposit(amount) #would also work
```

**Accessing Attributes**
Using getattr, we can look up an attribute 

**Methods and Functions**
Python distinguishes between:
- Functions, which we have been creating since the beginning of the ccourse, and
- Bound methods, which couple together a function and the object on which that method will be invoked
	- Object + Function = Bound Method

**Looking Up Attributes by Name**
expression, name

To evaluate a dot expression:
1. Evlaluate the expression to the left of the dot, which yields the object of the dot expression
2. name ...
3. ...

**Class Attributes**

