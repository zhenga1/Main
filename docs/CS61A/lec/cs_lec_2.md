Warren Hall can be used for CS 61a help
Types of expressions
Expression descrbes a computation and evaluates to a value
18+69
6/23
sqrt(3493161)

function call notation 
Call notaiton

Anatomy of call expression

THIS IS THE CALL EXPRESSION
-> add (2,3))
-> Operator(the function name) ( Operand, Operand )

Evaluation procedure for call exressions:

Evaluating nested expression
This is all jsut one call expression
		mul(add(4,mul(4,6)),add(3,5))
The operator is mul, the operands are add(4,mul(4,6)) and add(3,5) 
Call procedure is the operands. 

All arguments are values
Argument is just a number

Execution rule for assignment statements:
1. evaluate all expressions to the right of = from left to right.


Defining Functions
ssignment is a simple means of abtraction: binds names to values

Function definition is a more powerful means of abstraction: binds names to expression

Function definition is a more powerful means of abstraction: binds names to expressions
Function signature indicates how many arguments a function takes

-> def <name> <formal Paramenters>:
	return <return expressions>

Calling user-defined functions
Procedure for calling/applying user-defined functions (version 1):
1. Add a local frame, forming a new environemnt
2. Bind the functions' formal paramenters to its arguments in that frame
3. Execute the body of the function in that new environment

from operator import mul
def square(x):
	return mul(x,x)
square(-2)

Global frame 
mul  -> func mul(...)
square -> func square(x)

Original name of fucntion called
square
	x | -2
	return value 4
A function

Looking Up Names In Environment
Every expression is evaluated in the context of an environment.

So far, the ccurrent environemtn is either:
- The globl frame alone, or 
- A local frame, followed by the global frame

Most important two things I'll say all day:
An environment is a sequence of frames.

A name evaluates to the value bound to that name in the
 earliest frame of the curent environemnt in which that name is found.



