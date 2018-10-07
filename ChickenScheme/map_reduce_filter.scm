(define (divisible? x y) (= 0 (remainder x y) ))

(define (pe01)
  (reduce + 0 
	  ( filter
	    (lambda (x) (or (divisible? x 3) (divisible? x 5)))
	    (iota 1000)
	    )))

(print (pe01))
