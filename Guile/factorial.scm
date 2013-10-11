#!/usr/bin/guile \
-e main -s
!#

; by HVNSweeting <hvn@familug.org>
; on Fri Oct 11 09:08:54 ICT 2013

(define  (factorial n)
  (if (zero? n) 1 (* n (factorial (- n 1))))
  )

(define (display_factorial n)
  (display "Factorial of ") (display n) (display " is: ")
  (display (factorial n)) (newline)
  )

(define (main args)
  (display "Factorial Program") (newline)
  (display_factorial 5)
  (display_factorial 15)
  )

#!
hvn@archhvn: ~/Github/FAMILUG/Guile (master) $ ./factorial.scm
Factorial Program
Factorial of 5 is: 120
Factorial of 15 is: 1307674368000
!#
