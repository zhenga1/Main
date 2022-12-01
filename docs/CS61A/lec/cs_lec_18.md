**Special Forms**
A combination that is not a call expression is a special form:
- **if** expression: `(if <predicate> <consequent> <alternative> )`
- **and** and **or**       `(and <e1> .. <en>), (or <e1> ... <en>)`
- Binding symbols: (define `<symbol> <expression>`)
- New procedures: `(define (<symbol> <formal parameters>) <body>))`

```Scheme
> (define pi 3.14)
> (* pi 2)
6.28
> (define (square x) (* x x))
> (define (average x y) (/ (+x y) 2))
> (define (sqrt x) (define (improve guess)(average guess ( x guess))))
> 
```

**Lambda Expressions**
Lambda expressions evaluate to anonymous procedures
```Scheme
(lambda (<formal-parameters>) <body>)
(define (plus4 x) (+ x 4))
(define plus4 (lambda (x) (+ x 4)))
```
An operator can be a call expression too:
```Scheme
((lambda (x y z) (+ x y (square z))) 1 2 3 )
```
```Scheme
(define pi 3.14)
(define plus4 4)
(lambda (x) (+ x 4))
(define plus4 (lambda (x) (+ x 4)))
```

**Cond and Begin**
The **cond special form** that behaves like if-elif-else statements in Python. 
```Python
if x>10:
	print('big')
elif x>5:
	print('medium')
else:
	print('small')
```
```Scheme
(cond ((> x 10) (print 'big')) ((> x 5) (print 'medium')) else (print 'small'))

(print (cond ((> x 10) 'big') ((> x 5) 'medium') (else 'small')))
```

```Scheme
(define x 12)

(if (> x 10))
```
![[chrome_p30Kd4RRwj.png]]

**Let Expressions**
The let speccial form binds symbols to vlues temporarily; just for one expression
```python
a = 3
b = 2+2
c = math.sqrt(a*a+b*b)
```
![[chrome_lOTbA6qxAw.png]]
**Drawing Stars**
(forward 100) or (fd 100) draws a line
(right 90) or (rt 90) turns 90 degrees
![[chrome_CqBr7vzVYg.png]]
```scheme
(define (star n m) (let ((a (/ (* 360 m) n))) (define (side k) (if (< k n) (begin (fd 100) (rt a) (side (+ k 1)))))))(side 0))
```
