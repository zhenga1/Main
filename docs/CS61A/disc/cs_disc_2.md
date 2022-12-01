return print_all
Recursive function return 
If you return a recursive function then you can create another frame

Credit cards use Luhn algorithm
Sum of digits of 2022 is 6 ->
TASK: FIND ALL DIGITS OF SOME NUMBER, like 2022.
Break down into small tasks:
 	Sum all of the digits  = last digit + sum of digits of smaller number

Iteration vs Recursion
Iteration is a special case of recursion
	4! = 4*3*2*1 = 24
Using while:
def fact_iter(n):
total, k = 1,1
while k<=n:
total,k = total*k, k+1
return total

The recursive Leap of Faith
Is fact implemented correctly?
1. Verify the base case
2. Treat fact as a functional abstraction
3. Assume that fact(n-1) is correct
4. Verify that fact(n) is correct


Luhn sum 
take every second digit from the credit card, double it. 
If the doubled digit has value >9, then sum the digits of the double digit number
Take the sum of all the digits. If is multiple of 10, then it is valid credit card number
