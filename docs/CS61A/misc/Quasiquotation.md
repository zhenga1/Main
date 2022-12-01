Relating to the `quote` special form.

Usually, the `quote` special form tells us to not evaluate whatever is immeidately after the quote. However, the `quasiquote` form is slightly different, it allows both **quoting and unquoting** 

The **quasiquote** allows us to construct literal lists in a similar way as a quote, but also lets us specify if any subexpression within the list should be evaluated.

Consider that we rewrite the `twice` macro as follows:
```scheme
(define-macro (twice f) 
  '(begin f f))
```
This seems like it would have the same effect, but since the `quote` form prevents any evalaution, the result expression that is being created would actually be `(begin f f)`, which is not what is being wanted.

The **quasiquote** allows us to construct literal lists in a similar way as a quote, but also lets us specify if any expression within the list should be evaluated.

At first glance, the quasiquote (which can be invoked with the backtick or the **quasiquote** special form) behaves exactly the same as ' or `quote`. However, using quasiquotes gives you the ability to **unquote** (which can be invoked with a comma `,` or the `unquote` special form). THis removes an expression from the quoted context, evaluates it and places it back in.

By combining quasiquotes and unquoting, we can oten save ourselves a lot of trouble when building macro expressions.

Quasiquotes use thie backtick symbol
![[Pasted image 20221115164425.png]]
Whilst regular quotes are just '' these. 

Quasiquotes unquoting is basically the , mark, where we can have:
![[chrome_ZZDRl4R4Ew.png]]

![[chrome_MbqSzLEw0Q.png]]

Its like **define-macro** allows an unknown(unevaluated) scheme expression to be passed in as the parameter. Then, the define macro can be used to combine these expressions to form a bigger expression, which is then going to be evaluated.  

**define-macro**  allows us to define what's known as a **macro** which is just a simpler way for us to **combine unknown expressions together into another expression.** When we call macro, the operands of the expression are not evaluated but are instead treated as Scheme data. This means any operands that are call expressions  or special form expressions are treated as lists.

![[chrome_3XLk3ZQN30.png]]

**Regular lambda procedure:**
- Evaluate operator
- Evaluate operands
- Apply operator to operands, evaluating the bod of the procedure.

However, rules for evaluating calls to macro procedures are:
- Evaluate ooperator
- Apply ooperator to unevaluated ooperands
- Evaluate the expression returned by macro in the frame it was called in



