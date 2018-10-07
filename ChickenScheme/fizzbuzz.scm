(define (divisible? a b) (if (= 0 (remainder a b)) #t #f))
(define (fizzbuzz i) 
  (cond
   [(and (divisible? i 3) (divisible? i 5)) 'fizzbuzz]
   [(divisible? i 3) 'fizz]
   [(divisible? i 5) 'buzz]
   [else i]))


(for-each (lambda (i) (print (fizzbuzz i))) (iota 100))
