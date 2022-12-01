**Programs (in Python) as Data Mini-lec**
- Let's think about our code not as functions or expressions, but rather as data that we can manipulate!
Evaluation order can cause unintended side effects ..
```python
def list_5(expr):
	return f''[{e}]
```


```python
#One line if statement
[on_true] if [expression] else [on_false]
```

```python
def if_program(condition, true_result, false_result):
	return f"{true_result} if {condition} else {false_result}"
	
```
Important takeaway: We treat our lines like data!
	**Hint:** Can write one-line if statement with following syntax: 
	`<value_when_true> if <condition> else <value_when_false>`

# Scheme programs as Data
- Normal quote 'quote' and quasiquote `newer quote`
- If you use quasiquote, you can **unquote** specific parts of the expression using the comma , which will evaluate the parts after the comma !
Example:
```scheme
> (define a 5)
a
> (define b 3)
b
> `(* a b)
(* a b)
> `(* a ,b)
(* a, 3)
```

# Q3 If Program Scheme
Now let's try writing the `if_program` Python example using programs as data in Scheme! There are quite a few similarities between Python and Scheme, but we have to make a few adjustments when converting our code over to Scheme. We'll start out by writing a Scheme function with the `define` form we use for normal functions.

First, let's consider the following questions:

In the Python `if_program`, we returned a **string** that, when evaluated, would execute an `if` statement with the correct parameters. In Scheme, we won't return a string, but we'll return something else that can represent an unevaluated expression. What type will we return for Scheme? Here, what "type" refers to the data type: function, list, integer, string, etc..

``(if, condition, if-true, if-false)`
The output is still a list, but it would **not evaluate** everything after the first comma. 

```scheme
>(if_program `(= 0 0) `3 `5)
(if (= 0 0) 3 5)
>(if_program (= 0 0) 3 5)
(if #t 3 5)
```

![[WhatsApp Image 2022-11-09 at 6.28.41 PM.jpeg]]


