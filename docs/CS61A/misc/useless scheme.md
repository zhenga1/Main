```scheme
  `((define (func exp) (if (= nil exp) (nil) (append (car exp) (cdr exp))))

  (if ,condition (append 'begin func(,exprs)) (print 'okay)))
`(if ,condition (begin (car ,exprs)))

`(if ,condition (append '(begin) ,exprs) (print 'okay))
```

```scheme
  (if (= (eval expr) (car (car cases))) (cdr (car cases)) (switch expr (cdr cases)))
```

```scheme
(define-macro (switch expr cases)

  (cons eval

    (map ( (lambda (case) (= (car case) (eval expr))) (cons _________ (cdr case)))

          cases)

  )

)
```


```scheme
(define-macro (switch expr cases)

    (cons eval

        (map (lambda (case) (= (eval expr) (car case)) (cons list (cdr case)))

                cases))

)
```

Actually kinda useful
```scheme
    (cons 'eval

        (map (lambda (case) (cons `(if (not (= (car ,case) ,expr)) nil) (cdr case)))

                cases))
```

```scheme
    (cons 'eval
    (map (lambda (case) (cons (if (not (= (car case) expr)) nil) (cdr case)))

                cases))
```

```scheme
    (cons 'eval

        (map (lambda (case) (cons (list 'if (list = (car case) (expr)) nil 'eval)

         (cdr case)))

                cases)

    )
```
Working scheme code:
```scheme
(if (eval condition) (append (list 'begin) exprs) (print 'okay))
```

```scheme
    (cons 'begin

    (map (lambda (case) (cons

    (cons 'if

    (cons =

    (cons (list (car case))

    (cons expr

    nil)))) (cdr case))) cases

    )

    )
```

```scheme
((= (cdr s) nil) (car s))

  ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))

  

 (else (my-filter pred (cdr s)))

 )
```

```scheme
(+ (joiner start (term n)) (accumulate joiner 0 (- n 1) term))
```