#TailRecursion

# Tail Recursion

# Functional programming
-> The idea that you can organise entire programs into functions

We have that:
- All functions are pure functions
- No reassignment, no mutable data types
- Name-value bindings are permanant

Advantages of functional programming:
- The value of expression is independent of the order that the sub-expressions are evaluated
- Sub-expressions can be safely evaluated in order or on demand (lazily)
- **Referential Transparency:** Value of an expression does not change when you substitute one of its subexpressions with the value of the subexpression.
But, since there are no for/while statements as we cannot rebind variables to different values, how can we make recursion fast?

# Recursion vs Iteration in Python
In python, recursion always create new active frames.
`factorial(n,k)` computes `k*n!`

==Recursive solution:==
```python
def factorial(n,k):
	if n==0:
		return k
	else:
		return factorial(n-1,k*n)

```
Up to $n$ frame,s time $\Theta n$ and space $\Theta n$ 

==Iterative solution==
```python
def factorial(n,k):
	while n>0:
		n,k = n-1, k*n
	return k
```
Only one frame, time $\Theta n$ but space $\Theta 1$ 


**Summary:**
-  Two functions can have same runtime and different memory usage
-  Iterative functions use less space because they only have one frame

But what about Scheme? We have no iteration!

# Tail Recursion
"Implementation of scheme is allowed to be properly **tail-recursive**. This allows the execution of an **iterative computation in constant space**, so even if the iterative computation is described by a **syntactically recursive procedure**"

A.K.A

Since Scheme **doesn't actually have an iterative way to write code**, we must figure out a way to use *less space* in Scheme but still do recursion.

So this is where **tail recursion** comes in!!

![[chrome_WFeUFm3Cxh.png]]
We see that the above expression in scheme (*recursive*) should use the same resources as the below python script. HOW TO DO??
![[chrome_e9odYn4cL5.png]]
All the frames on the top **are essentially useless** once the next recursive call is made, since there is no need to keep those frames anymore. Unlike certain cases when tail-recursion is not possible (such as finding a unique path through a map), in this factorial instance, tail-recursion is the best solution, since there is no need to keep around frames that have data that can be discarded.

# Tail Calls
If there is nothing to do beside return the result of the recursive expression in the parent frame, then the function call is **tail-recursive**
In other words:
```python
def tail_recursive(thing):
	###STUFF
	return tail_recursive(thing-1)
	###Nothing to do after recursion, no other implementations/code
```
**Tail Call:**
A *procedure call* that has not yet returned is ==active==. Some procedural calls are *tail calls*. A Scheme interpreter should support an *unbounded number* of active tail calls using only a *constant* number of space.

A tail call is a call expression in a *tail context*
- The last body sub-expression of a lambda expression
- Sub expression 2 or 3 can also be in a tail context in an **if** expression. 
- All non-predicate sub-expressions in a tail-context **cond**
- The last sub-expression in a tail-context **and** or **or**
- The last sub-expression in a tail-context **begin**

## Example: Length of a List
```scheme
(define (length s) 
  (if (null? s) 0
  (+ 1 (length (cdr s)))
  ))
```
A call expression is not a tail call if more computation is still required in the calling procedure

We see above the result of `(length (cdr s))` is being used and summed with the expression 1, so it is not properly **tail recursive**

So, the call above requires linear space.

![[chrome_f5bJU4ko1Q.png]]

So doing the adding of $n$ within a **nested inner function**. 

![[chrome_7H3FqogQeZ.png]]

SO basically, we have the above is a call in tail-context.

# Eval with Tail Call Optimization
The return value of the tail call should be the return value of the current procedure call.

Therefore, tail call shouldn't increase the environment size.


### Example: Define factorial function that returns n!$\cdot$  k
(tail call):
```scheme
(define (factorial n k) 
  (if (zero? n) k (factorial (- n 1) (* n k)))
)
```
Not optimized for tail calls

We see that , we can have:
```scheme
> (factorial 10 1) # DOABLE
> (factorial 100 1) # DOABLE
> (factorial 1000 1) # ERROR, MAXIMUM DEPTH EXCEEDED
```
So basically scheme interpreter is not **tail-recursive**
WE **should be able** to compute this as much times as we need, there shouldn't be a recursive error.

![[chrome_UdMFbO9Kbo.png]]
We see that, out of the following functions:
- `length` is not tail-recursive, since the expression that contains the **tail-recursive** statement is added to **1**, meaning it is not in **tail-context**, there is something that needs to be done after the function is called.
- `contains` is tail-recursive, since the if expression that contains the **recursive call** is at the tail.
- `has-repeat` is tail-recursive. This entire if expression is in a **tail-context**, so we have that `has-repeat` must be **tail-recursive**.
- `fib` is not tail recursive, since the **inner** function `(fib (- k 1))` is not a function in **tail-context**

### Examples: Looking at higher-order functions
`(define (reduce procedure s start))`
Basically applies the procedure from start to each and every element within the list `s`. Essentially it reduces a list `s` and integer `start` to a single thing, whether that be a list or a number or something else. 

Example: 
`(reduce * '(3 4 5) 2)` 
-> Effectively this computes $2\cdot 3$, then   $(2\cdot 3)\cdot 4$, etcetera, until we get the final answer of $120$.

`(reduce (lambda (x y) (cons y x)) '(3 4 5) 2`
-> Effectively we first do `(cons 2 3)`, then we do `(cons 4 (cons (2 3)))`, then finally we do `( cons 5 (cons 4 (cons (2 3))))`. So the end result becomes:
`'(5 4 2 3)`

![[chrome_OK3sdycoGU 1.png]]
From above image, we see that both *Box 1* and *Box 2* are in tail context. However, **RED BOX** is not, as the *procedure function* is being called and then the result is being passed in to the *result* function.

Hence, does this run in constant time? Maybe.
$\rightarrow$ This is entirely dependent on whether or not the **RED BOX** runs in constant time and requires only constant space. If only requires constant space, then the entire function **reduce** requires only constant space. If not, then no.

### Example: Map with only a constant number of frames
`map` function basically takes in a procedure and a list, and creates a new list whereby the procedure is applied to every element of the list. It is assumed that the procedure can be applied to every element in the list
```scheme
(define (map procedure s)
  (if (null? s) nil
  (cons (procedure (car s)) 
  (map procedure (cdr s))))
)
```
We see that **map** is obviously not a **tail-context**, since whatever is returned from the **map** function is passed directly into **cons**.

HOW TO MAKE IT TAIL RECURSIVE?
SOLUTION:
```scheme
(define (map procedure s)
  (define (map-reverse s m)
  (if (null? s) m 
  (map-reverse (cdr s) (cons (procedure (car s)) m))
  )
  )
  (reverse (map-reverse s nil))
)
```
We see that the `reverse` call isn't **tail-recursive**, but then the calls to **map-reverse** is **tail-recursive**, so we are good. Since the function called is **map-reverse** instead of **map** for the function call within the **reverse**, we see that that not being tail-recursive is insignificant. 

What about the **reverse** function?
```scheme
(define (reverse s)
  (define (reverse-iter s m)
  (if (null? s) m
  (reverse-iter (cdr s) (cons (car s) m)))
  )
)
```

## What is it we are doing when we create interpreters?

We are creating little machines. 

#### An analogy: Programs define machines
Programs specify logic of computational devices.
![[chrome_jR2pEkfBj4.png]]
## Interpreters are General Computing Machines

An interpreter can be parameterized to simulate any machine

Our scheme interpreter is a universal machine. 

Think of it as a bridge between data objects that are manipulated by our progrmaming language and the programming language itself. 

Internally, it is just a set of evaluation rules.

# Dynamic Scope
The way in which names are looked up in Scheme or Python is called *lexical scope*. (or *static scope*)

**Lexical Scope:** The parent of a frame is in the environment in which a procedure was *defined*

**Dynamic Scope:** The parent of a frame is the environment in which a procedure was *called*.
![[chrome_Gzn9wEJyoh.png]]

