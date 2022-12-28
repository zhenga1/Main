Notes:
- Apparently `let` has the following syntax:
`(let (#definitionexprs) (returned expr))`
Lets say we want to define $x = 5$, $y = 6$ in a local frame, and then return their sum. We can do:
`(let ((x 5) (y 6)) (+ x y))`

## Example: While statements
Sum of squares of even numbers less than 10, beginning with 2

```scheme
(begin (define (f x total) 
  (if (< x 10)
  (f (+ x 2) (+ x total)) 
  total)
)
(f 2 0)
)
```

Sum of squares of numbers whose square is less than 50, beginning with 2
```scheme
(begin 
(define (f x total)
  (if (< (* x x) 50) 
  (f (+ x 1) (+ total (* x x)))
  total
  )
)
 (f 2 0)
)
```

NEW TASK: WE WANNA CREATE A FUNCTION THAT RETURNS AN EXPRESSION THAT DOES THE ABOVE
```scheme
(define (sum-while initial-x condition add-to-total update-x)
  `(begin (define (f x total)
  (if ,condition (f ,update-x (+ total ,add-to-total))
  total
  )
)
```
![[chrome_5ulud6mK3O.png]]
