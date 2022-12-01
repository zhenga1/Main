# Interpreter
An **interpreter** is a program which can directly execute instructions in a programming language like Python or Scheme. To do this, the interpreter needs to understand how the rules of a language work, and to do that, the interpreter needs to be designed (by a human, usually!) to follow those rules. In CS 61A, we'd like to learn how the interpreter _program_ works and understand the ideas that go into an interpreter to reveal the magic behind how a computer makes sense of `(+ 1 2)` in Scheme and `1 + 2` in Python.

### REPL

The interpreters we study in this course are designed around a **Read-Eval-Print-Loop**.

The interpreter waits for our input, looping until we type in a string of characters, `(+ 1 2)`.

1.  In the **Read** stage, we take the string of characters and convert those characters into data structures that can be understood by the interpreter. In the Scheme interpreter, we'd like to take the string of characters `(+ 1 2)` and convert it into a `Pair` structure, `Pair('+', Pair(1, Pair(2, nil)))`.
    
    -   The **Lexer** takes the string `(+ 1 2)` and splits into meaningful _tokens_ wherever there is whitespace or a syntax character like the open parenthesis `(`. The lexer returns a structure that kind of resembles a list of individual characters like `['(', '+', 1, 2, ')']`.
    -   The **Parser** takes the list of smaller strings and converts them into a data structure that understands the nesting in the language. It's not too tricky to convert the example above from `['(', '+', '1', '2', ')']` to `Pair('+', Pair(1, Pair(2, nil)))`. But the pair structure is much more useful when we want to work on a more nested example like `(= (+ 1 2) 3)` which the lexer converts into the flat list `['(', '=', '(', '+', 1, 2, ')', 3, ')']`. As the expressions get more and more complicated, using a nested data structure helps the computer make sense of the expression in chunks, much like how we humans make sense of a Scheme expression as well.
2.  In the **Eval** stage, we evaluate the nested data structure to a value.
    
    -   If the expression is simple, like a number or a boolean, we can just return the number or boolean itself without any further evaluation. Evaluating 1 in the global frame returns the number `1`. If we pass in a name like 'x', we'll try to evaluate the name 'x' in the current environment, looking up through the parent frames as necessary.
    -   If we pass a call expression like `Pair('+', Pair(1, Pair(2, nil)))` into the evaluator, we'll follow the call expression evaluation rules to determine the value of the value of the expression. We'll evaluate the operator, `'+'`, to the built-in procedure which adds values, and each operand, 1 and 2, before applying the procedure to the arguments.
    -   if the expression is a special form like `Pair('define', Pair('x', Pair(1, nil)))` (after parsing `(define x 1)`), then we'll follow the special form evaluation rules defined in the Scheme interpreter. In this example, we don't need to evaluate the name 'x' (it's just a name!) but we do need to evaluate the value, the number `1`.
3.  In the **Print** stage, we take the value we determined in the evaluation stage and figure out how to display the value to the user. Even if an expression evaluates to a number, the computer actually stores that number in its memory as a bunch of 0 and 1 binary digits! We take that number and convert it back to a more readable representation like '3'!
4.  Once we've displayed the value, we can wait in a **Loop** until the user asks another question to the interpreter.

There are some special rules in the parser to handle scenarios like the quote operator `'`. Run `python3 scheme_reader.py` to explore its behavior.

```
read> '1
str : (quote 1)
repr: Pair('quote', Pair(1, nil))
read> '(1 2 3)
str : (quote (1 2 3))
repr: Pair('quote', Pair(Pair(1, Pair(2, Pair(3, nil))), nil))
```

Likewise, the evaluator also needs to handle the behavior of special forms differently from standard call expressions. The [Scheme Specification](https://cs61a.org/articles/scheme-spec/#special-forms) contains more information, and the special form evaluation rules will also be briefly described by example here.
