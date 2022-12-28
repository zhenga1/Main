```scheme
(define (make-necklace beads length)
  (if (= length 0) nil
  (cons (car beads) 
  (make-necklace (append (cdr beads) (list (car beads)) (- length 1)
)))
)  
)
```