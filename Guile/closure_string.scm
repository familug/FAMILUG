#!/usr/bin/guile \
-s
!#

; An ugly example append string use closure to create two
; procedures that can both access a base string
; by HVNSweeting <hvn@familug.org>
; Mon Oct 14 23:35:55 ICT 2013

(define append-name #f)
(define append-job #f)


(let ((sentence "Hello"))
 (set! append-name
  (lambda (name)
   (set! sentence (string-append sentence " I'm " name "."))
   sentence
   ))

 (set! append-job
  (lambda (job) (set! sentence (string-append sentence " I'm " job "."))
   sentence)
  )

 )

(append-name "HVN")
(display (append-job "a programmer")) (newline)

#!
hvn@archhvn: ~/Github/FAMILUG (master) $ guile Guile/closure_string.scm
Hello I'm HVN. I'm a programmer.
!#
