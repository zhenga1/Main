Warren Hall can be used for CS 61a help

A function that does not expliitly return a value will return None
Careful: None is not displayed by the interpreter as the value of an expression

None is not displayed by the interpreter as the value of an expression (only value to do so) look at line 3
Functions end at return statement
```Python
return  #is the same as 
return None.
```


Pure functions and Non-Pure Functions
Pure Functions
given the same input, the function will return the same output
Just return vlaues

Non-Pure Functions
will not really return the same output for every given input 
have side effects -> return none
Not jsut returning a value, it also does other stuff, like prints someething out

Print prints stuff out all on  one line and then goes to the next line
Multple environments:
- Sequence of frames which show bindigns of names and values

Def statement:
```Python
def square(x):
	return mul(x,x)

>>>square(2+2)
```

What happenes?
A new function is creted!
Name bound to that function in the current frame

Call expression: square(2+2) Operand 2+2, argument: 4
Operator: Square
Function: func square(x)

Calling/Applying: Argument. x will evaluate to 4
Signature -> Square(x)

```Python
from operator import mul
def square(x):
	return mul(x,x)
square(square(3))

	Global frame:
		mul
		square
	f1: square [ parent-Global]
		x:3
		return value:9
	f2: square [ parent=Global]
		x:9
		return value:81
```




First you must look at the parent Frame, as in the primarily local(square) frame.
If not found, then look in the Global frame, which includes the functions, such as mul and square

n enviornment is a sequence of frames
- the global frame alone
- A local, then the global frame

Square(square(3)) -> func square(x) 
-> square(3) --> func square(x) ->
|
>3

In this case, there is only two frames, specifically the local and then the global frame.

NAMES HAVE DIFFERENT MEANINGS
```Python
def square(square):
	return mul((->two)square,square)
```


square(4) <- one

so basically the one square is in the global frame, so square refers to the method
but the square inside of the square function searches the local frame, so square refers to the parameter of the function 
square.


```
python3 -m doctest ex.py
```

This is using the doctest lines and testing them, seeing if they are correct.

INFINITE LOOP cuz even negative numbers 
if negative -> True

Evaluating short-circuit codes
once the code reaches the end of the truthy statements, it kills itslef
So the code finishes execution
 at the last truthy statement
WIth the and sequence
if 5 and 0 and 20 -> with and, everything following must evaluates to a truthy value

if False or 0 or 20   -> Or thingy stops at the last non-truthy value

 Print with 'DEBUG:' at the front of the outputted line to avoid ok from grading 

