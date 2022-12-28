Function mostly have global parent.

Calling every function always 
- creates a new frame
- Binds formal parameters (f&x) to arguments
- Execute the body:

```Python
	return f(f(x))
```

- Every user-defined function has a parent frame(often global)
- The parent of a function is the frame in which it was defined
- Every local frame has a parent frame (often global)
- The parent of a frame is the parent of the function called

-> You must call the outer(parent) function before you can call or get access to the inner function
Anything that was not indented is evaluated in the global frame.
Anything indented might be evvaluated in the local frame

Python's job is to figure out frames which to quit and which to keep

There are sometimes that you know one argument early, one argument late. So you want another function nested within the 
function, that can deal with all the operations of the function after all the arguments are known.

Like for example in the hog game, you may know your own score temporarily, but you may not know the score of your opponent
So you can call the outer function first, and call the nested function after you know the score of your opponent.

Scope = all the stuff that you can refer to

HOw to draw an environment diagram:
When a function is defined:
- Create a function value: 

```html
func <name>(<formal parameters>) [parent = <label>]
```

Is parent is the current frame
	f1: make_ader 		func(adder)

When you evaluate a function, you always first evaluate the operator and operand subexpressions 
2. Then you must apply the function that are the value of the operator to the 
argument that are the values of the operands

List : is a container, something that contains other values

```Python
add(list1, list2) 
# adding two lists, basically extending/equivalent to list1.extend(list2)
```


```Python
mul(list,number) #adding list number times.
```


Continuous comparisons(consecutive comparisons), is basically each comparison and everything else.
SO for example:
$a<b<c<d<e$ evaluates:
1) whether $a<b$
2) whether $b<c$
3) whether $c<d$
4) whether $d<e$

```Python
def skip_mul(n):
    if n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)
```


ERROR IS BASICALLY THAT ONE BASE CASE IS NEGLECTED. This above function will work for even numbers but,
for odd numbers, we see that the function will never stop and will recurse forever as it will never meet a base condition. The base condition $n==1$ should be added but is not.