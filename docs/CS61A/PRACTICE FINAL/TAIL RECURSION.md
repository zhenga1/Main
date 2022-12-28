### Question 1

Write a function `map` that is tail recursive. It should take in a list `lst` and a function `fn`, and apply the function onto every element in the list.
MY ANSWER:
```scheme
(define (map fn list)
  (define (map-iter s m)
  (if (null? s) m
  (map-iter (cdr s) (cons (fn (car s)) m))
  )
  )
  (reverse (map-iter list nil))
)
```
Better answer, without using **reverse**
```scheme
(define (map fn list)
  (define (map-iter s m)
  (if (null? s) m
  (map-iter (cdr s) (append m (list (fn (car s))))))
  )
  (map-iter list nil)
)
```

### Question 2

Write a function `filter` that is tail recursive. It should take in a list `lst` and a function `pred`, and keep only the elements in the list that satisfy the predicate.

MY ANSWER:
```scheme
(define (filter pred lst) 
  (define (filter-iter s m)
  (cond ((null? s) m) 
  ((pred (car s)) 
  (filter-iter (cdr s) (append m (list (car s)))))
  (else (filter-iter (cdr s) m))
  ))
  (filter-iter lst nil)
)
```

OFFICIAL ANSWER:
```scheme
(define (filter pred lst) (define (filter-help lst so-far) (cond ((null? lst) so-far) ((pred (car lst)) (filter-help (cdr lst) (append so-far (list (car lst))))) (else (filter-help (cdr lst) so-far)))) (filter-help lst nil))
```

### Question 3

Write a function `insert` that is tail recursive. It should take in a list `lst`, an `item`, and an `index`, and insert the `item` into the list at the given `index`.

MY ANSWER:
Ver 1
```scheme
(define (insert lst item index)
  (define (insert-iter s m index)
  (cond ((null? s) 
  (append m (list item)))
  ((= index 0) 
  (insert-iter (cdr s) (append m (append (list item) (list (car s)))) (- index 1))) 
  (else 
  (insert-iter (cdr s) (append m (list (car s))) (- index 1))
  )
)
)
  (insert-iter lst nil index)
)
```
Ver 2:
```scheme
(define (insert lst item index)
  (define (insert-iter s m index)
  (if (or (null? lst) (= index 0))
   (append m (cons item s))
   (insert-iter (cdr s) (append m (list (car s))) (- index 1))
	)
)
  (insert-iter lst nil index)
)
```

BETTER SOLUTION:
```scheme
(define (insert lst item index) (define (insert-help lst index so-far) (if (or (null? lst) (= index 0)) (append so-far (cons item lst)) (insert-help (cdr lst) (- index 1) (append so-far (list (car lst)))))) (insert-help lst index nil))
```

### Question 4

Write a function `remove` that is tail recursive. It should take in a list `lst` and an `item`, and remove the first occurence of `item` in the list. If `item` item doesn't occur, just return the original list.

```scheme
(define (remove lst item) 
  (define (remove-thing s m)
  (if (= (car s) item)
	  (append m (cdr s))
	  (remove-thing (cdr s) (append m (list (car s)))))
  )
  (remove-thing lst nil)
)
```

```scheme
(define (remove lst item)
  (define (remove-thing s m)
  (if (= (car s) item) 
	  (append m (cdr s))
	  (remove-thing (cdr s) (append m (list (car s))))
  )
  )
  (remove-thing lst nil)
)
```

```scheme
(define (remove lst item)
  (define (remove-thing s m)
  (cond ((null? s) m)
  ((= (car s) item) (append m (cdr s)))
  (else (remove-thing (cdr s) (append m (list (car s)))))
  )
  )
  (remove-thing lst nil)
)
```

### Question 5

Write a function `pop` that is tail recursive. It should take in a list `lst` and an `index`, and remove the item in the list at the given `index`. If the index is out of bounds, just return the original list.

```scheme
(define (pop lst index)
  (define (pop-help s m index)
	  (cond 

	   ((null? s) m)
	   
	  ((= index 0) 
	  (append m (cdr s)))

	   (else (pop-help (cdr s) (append m (list (car s))) (- index 1)))
	  )
  )
  (pop-help lst nil index)
)
```