#r/lecture
- Lecture notes: link

# Lecture: 10/10
```jupyter
print("Hello world i am cool")
```

# Attributes
**Terminology: Attributes, Functions and Methods**
- All **objects** have attributes, which are name-value pairs
- **Classes** are objects too, so they have attributes
- *Instance attribute*: attribute of an instance
- *Class attribute*: attribute of a class
	- probably equivalent to methods and **static** objects in Java.

**Terminology:**
![[chrome_PBI7Kk8h3w.png]]

**Python Object System**
- **Functions** are objects.
- **Bound methods** are also objects: a function that has its first parameter "self" already bound to an instance (of the class)
- **Dot expressions** evalate to bound methods for class attributes that are functions. 
	- Example: 
		- instance.method_name
**Looking up attributes by name(reminder)**
expression . name
To evaluate dot expression
1. Evaluate expression to the left of the dot, which yields the object(required)
2. Name is matched against the instance attributes of that object; if an attribute with that name exists, its vlaue is returned.
3. If not, name is looked up in the class, which yields a class attribute value
4. That value is returned unless its a function, in which case a bound method is returned instaed

Assignment statements with a dot expression on their left-hand side affect attirbutes for the objet of that dot expression.
- If the object is **instance**, then assignemnt set sinstance attribute
- If object is **class**, then assignment sets a class attribute.
**Instance attribute assignment example:**
![[chrome_xR4KuTK9I4.png]]
'interest' is an instance attribute, since the object of the dot expression(the first thing before the dot) is *tom_account*, which is an instance (of class Account)

The name (*interest*) is not looked up in the class. In fact, *tom_account* didn't even have an attribute *interest*, only *holder* and *balance*, since it wasn't defined in the constructor. 

So basically python creates a new attribute called *interest* under *tom_account*. 

**Class attribute Assignment**
![[chrome_T9WDh3sCM3.png]]
*Account* exists and is a class, so this is class attirbute assignment. Since the *interest* attribute already exists, that attribute under *Account* will be modified.

**Attribute Assignment Statements**
 **For class assignemnt**
 ![[chrome_eh7xEeJrw3.png]]
 So *interest* is the attribute for every class.
 (withdraw, deposit) are methods.
![[chrome_S3ePVAH28r.png]]
As seen above, we see that the *interest* attribute is not static and can be changed, and thsi change will be reflected in all of the *instances* of the class *Account*
 **For instance assignemnt**
![[chrome_POhwzuOr54.png]]
- Instance assignment attributes in different objects are different and can take on different values, even if both instances involved are objects of the same class
- The instance assignment (name) can be the same as a class attribute, and that will be completely fine. The assignment of the attribute for the instance is independent from the class attribute. 

**Inheritance**
Inheritance -> Relating classes together
Common use: Two similar classes differ in degree of specialization.
1) Specialized class may have same attributes as general class, along with special-case behaviour
2) New subclass "shares" attr with base class
3) Subclass may *override* inherited attributes, class or instance.

**Example Inheritance**
Checking account -> specialized Account (with interest cuz banks are trash)
 ![[chrome_rPc9uMpm0X.png]]
 1) Basically regular account, but withdraw method is stlightly different. 
 2) Perfect solution is to have the Checking account extend/inherit from Account, but overriding the *withdraw* method to add the fee which is why banks are trash
 **Extending in python example below:**
![[chrome_d9njr1ZSxy.png]]
Base class attributes aren't copied into subclasses!
To look up name in class:
1. If it names attribute in class, return attribute
2. Otherwise, look up name in base class, if there is one.
![[chrome_ZHcNRwryPE.png]]
**Noob implementation(w.o extend of base class method):**
![[chrome_32M7XkEWus.png]]
**Dominant implementation**
![[chrome_URDxhHACbk.png]]
- *Using parent method to accomplish goals*
![[chrome_dsiFyxJF8Z.png]]
![[chrome_maVQTUafYY.png]]

**Inheritance & Composition**
![[chrome_5BwlHsh1MR.png]]

![[chrome_rItrPfyV0y.png]]

**Designing for Inheritance**
![[chrome_Gzh4lLrqDC.png]]
![[chrome_Cjd2iC5jD0.png]]

WTF:
![[chrome_1KOYMYwIKm.png]]

**Multiple Inheritance**
![[chrome_32s8dM7gHq.png]]
![[chrome_1yvg4wQuEl.png]]

![[chrome_JPeGZE4j1g.png]]
Only thing we need to know is that methods will first be pulled from the (first level parents class), rather than the upper levels parent class.

*There is a particular order in which you look at all of this. To find (attributes, methods, etc), all one needs to know is that you look in the subclasses before you look at the base class* - John DeNero.
