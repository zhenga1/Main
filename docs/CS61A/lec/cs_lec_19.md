**Scheme** is a dialect of **Lisp**

**Scheme programs** consist of expressions, which can be:
- **Primitive expressions:** 2, 3.3, true, +, quotient, ...
- **Combinations:** (quotient 10 2), (not true), etc

**Numbers** are *self-evaluating*, whilst **symbols** are bound to **values**
**Call expressions** include an *operator* and *0 or more operands* in parenthesis. 

```scheme
> (quotient 10 2)
5
> (quotient (+ 8 7) 5)
3
> (+ (* 3 ()))
```
"quotient" names Scheme's built-in integer division procedure (i.e. function)
![[chrome_TPrim4rfNQ.png]]
One can also combine **expressions** throughout **many lines**, as long as the expressions are closed correctly(spacing doesn't matter). All it matters is that you **close** **parenthesis** that you open. 

```scheme
> 2
2
> (+ 1 2 3 4)
10
> (+)
0
> (* 1 2 3 4)
24
> (*)
1
> (* 2 2 2 2 2 3 3 3)
864
> (- (* 2 2 2 2 3 3 3) 1)
> (number? 3)
#t
> (number? +)
#f
> (zero? 0)
#t
> (zero? 2)
#f
> (integer? 2.2)
#f
> (integer? 2)
#t
```

**Special Form:**
A combination that is not a call expression is a **special form**
- **If** expression. (`if <predicate> <consequent> <alternative>`)
- **And** and **or** (`and <e1>, <e2>, ... <en>`), (`or <e1>,<e2>, ... ,<en>`)
- Binding symbol: (`define <symbol> <expression>`)
- New procedures: (`define (<symbol> <formal parameters>) <body>`)

```scheme
> define (square x) (* x x)
square
#We have defined the procedure square 

> (square 16)
256
> (define (average x y) (/ (+ x y) 2))
average
> 
```
`define pi 3.14`
`define (square x) (* x x)`

**Lambda expressions**
Lambda expressions evaluate to **anonymous procedures**
Two equivalent expressions for a plus 4 procedure:
`(define (plus4 x) (+ x 4))`
`(define plus4 (lambda x (+ x 4)))`


![[chrome_X1HkJkdgbA.png]]
The **cond** special form behaves as an if-elif-else statements in Python
```scheme
> (cond ((> x 10) 'big)
> (> x 5) 'medium))
```
![[chrome_6ecR99LzGL.png]]
# Let Expression
The let special form binds symbols to values **temporarily**, just for one expression.
```Python
a = 3
b = 2+2
c = math.sqrt(a*a + b*b)
# a and b are still bound down here
```
![[chrome_8BwSa7GGxe.png]]

# Sierpenski's triangle
![[chrome_IJZMY5hWem.png]]


# Scheme Lists
**Scheme** has **lists**, and lists in Scheme are like the **LinkedList** class in python. 

In the late 1950s, computer scientists use confusing names
- **cons**: Two argument procedure that creates a linked list. 
- **car**: Procedure that returns first element of a list.
- **cdr**: Procedure that returns the rest of the list
- **nil**: The empty list. 

Scheme lists are **written in parenthesis** with **elements separated by spaces**. 
![[chrome_slSxg6DUGL.png]]
# Symbolic Programming
Symbols normally refer to values; how to refer to symbols?
```scheme
> (define a 1)
> (define b 2)
> (list a b)
(1 2)
```
**Quotation is used to refer to symbols directly in LISP.**
```scheme
> (list 'a 'b)
(a b)
> (list 'a b)
(a 2)
```

![[chrome_aLiymWLI94.png]]

![[chrome_DbmrR9BJsS.png]]

# Even Subsets
**Definition:** a *non-empty subset* of a list **s** is a list containing some of the elements of **s**.
(A *non-empty subset* could contain all of the elements of **s**, but not none of them )
![[chrome_HgF6zZEIUt.png]]

![[chrome_5d7E1RpU41.png]]
![[I7xxw0VeFp.png]]
# Raise Exception
Python exceptions are raised with a raise statement.
``raise <exception>``
`<exception>` must evaluate to a subclass of BaseException or an instance of one

Exceptions are constructed like any other object. 
![[chrome_84Sqoalbh5.png]]
# Try Statements
Try statements handles exceptions:
```python
try:
	<try suite>
except <exception class> as name:
	<except suite>
```
**Handling Exceptions**
```python
>>> try:
		x = 1/0
	except ZeroDivisionError as e:
		x = 0	
```

![[chrome_CLCD7LVwNT.png]]


**Scheme** is a programming language that has few rules. 

# Programming Languages
A computer typically executes program written in many different programming langauges

**Machine Languages:** statements are interpreted by the hardware itself
- A fixed set of instructions invoke operations implemented by the circuitry of the central processing unit(CPU)
- Operations refer to specific hardware memoray addresses; no abstraction mechanisms
**Higher level languages** statements & expressions are interpreted by another program or compiled (translated) into another language.
- Provide means of abstraction such as naming, ufnction defintion, and objects. 
- Abstract away system details to be independent of hardware or operating systems

# Metalinguistic Abstraction

A powerful form of abstraction is to define a new language that is tailored to a particular type of application or problem domain.

**Type of application:** Erlang was designed for concurrent programs. It ahs built-in elements for expressing concurrent communication. It is used, for example, to implement chat servers with many simulatenous connections.

**Problem Domain** The MediaWiki markup language was designed for generating static web pages. It ahs built-in elemnets for text formatting and cross-page linking. it is uesed, for example, to create Wikipedia pages.

A programming language has:
- **Syntax**: the legal statements and expressions in the lagnauge
- **Semantics**: The execution/evaluation rule for those statemnets and expressions
To create a new programming langauge, you either need a:
- **Specification**: A document decribin the precise syntax and semantics of the language
- **Canonical Implementation**: An interpreter or complier for the language.

## Part 3: Special Forms

This section will be completed in `scheme_forms.py`.

Logical special forms include `if`, `and`, `or`, and `cond`. These expressions are special because not all of their sub-expressions may be evaluated.

In Scheme, only `#f` is a false value. All other values (including `0` and `nil`) are true values. You can test whether a value is a true or false value using the provided Python functions `is_scheme_true` and `is_scheme_false`, defined in `scheme_utils.py`.

> Scheme traditionally uses `#f` to indicate the false Boolean value. In our interpreter, that is equivalent to `false` or `False`. Similarly, `true`, `True`, and `#t` are all equivalent. However, **when unlocking tests**, use `#t` and `#f`.

To get you started, we've provided an implementation of the `if` special form in the `do_if_form` function. Make sure you understand that implementation before starting the following questions.

# The Structure of an Interpreter
It shares a lot with calculator example
There is an **Eval** and an **Apply** function. 

# **Eval**
Base cases:
- Primitive values (numbers)
- *Look up values bound to symbols*

Recursive calls:
- Eval(operator, operands) of call expressions
- Apply(procedure, arguments)
- *Eval(sub-expressions) of special forms*
This is going to require an environment for symbol lookup.

# Apply
Base cases;
- Built-in primitive procedures
Recursive calls:
- *Eval(body) of user defined procedures*
Creates a new environment each time a user-defined procedure(like a lambda function) is applied 

# Scheme Evaluation
The **scheme_eval** function dispatches on expression for form:
- Symbols are bound to valeus in the current environment
- Self-evaluating expressions are returned
- All other legal expressions are represented as Scheme lists, called combinations. 

```python
(if <predicate> <consequent> <alternative>)
(lambda (<formal-parameters>) <body>)
(define <name> <expression>)
(<operator> <operand 0> ... <operand k>)
(define (demo s) (if (null? s) '(3) )
```
![[chrome_MZ7cWIlUok.png]]

# Logical Special Forms
Logical forms may only evaluate some sub-expressions.
- **If** expression: `if <predicate> <consequent> <alternative>`
- **And** and **or**: (`and <e1> ... <en>`)     (`or <e1> ... <en>`)
- **Cond** expression: (`cond (<p1> <e1>) ... (<pn> <en>)`)

The value of an **if** expression is the value of a sub-expression.
- Evaluate the predicate
- Choose a sub-expression: `<consequent>` or `<alternative>`
- Evaluate that sub-expression in place of the whole expression. 

# Quotation
The **quote** special form evaluates to the quoted expression, which is **not evaluated**

The `<expresssion>` itself is the value of the expression
`'<expression>` is shorthand for (`quote <expression>`)

# Define Expressions
Define binds a symbol to a value in the first frame of the current environment:
`(define <name> <expression>)`
We define the following procedural steps
1. Evaluate the `<expression>`
2. Bind `<name>` to its value in the current frame.
**Procedure definition:** 
- Shorthand of define with a lambda expression
`(define (<name> <formal parameters>) <body>)`
This above is equivalent to:
`(define <name> (lambda (<formal parameters>) <body>))`

# Applying User-defined procedures
To apply user-defined procedure, we must create a new frame bound to argument values, whose parent is the **env** of the procedure.

Evaluate the body of the procedure in the environemnt that starts with this new frame.
```scheme
(define (demo s) (if (null? s) '(3) (cons (car s) (demo (cdr s))) (demo (list 1 2))
```


