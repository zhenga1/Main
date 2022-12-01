procedure: **cons** _obj1 obj2_

Returns a newly allocated pair whose car is obj1 and whose cdr is obj2. The pair is guaranteed to be different (in the sense of `eqv?`) from every previously existing object.

``(cons 'a '()) ``                          =>  (a)
``(cons '(a) '(b c d))      ``              =>  ((a) b c d)
``(cons "a" '(b c)) ``                      =>  ("a" b c)
``(cons 'a 3)     ``                        =>  (a . 3)
``(cons '(a b) 'c)             ``           =>  ((a b) . c)

# Ways of defining various expressions:
`(begin (foo) (bar))` is a scheme expression that will run each subsequent expression within the `()` of begin, and returns the evaluation of the last expression.
