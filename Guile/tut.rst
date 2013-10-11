Scheme
======

* Latently typed (Latent typing)
  you cannot, in general, simply look at a program's code and determine what
  type of data will be associated with a particular variable/ expression.

* Data types
  Primitive: chars, strings, numbers, procedures.
  Compound: lists, pairs, vectors, multi-dim arrays.
  Your own data type

Every value "knows" at runtime, what type of it.
A variable, has no fixed type. A var, is name of a location - a box.

* Defining and setting var
  (define var-name value)
  (define x 5)
  (set! x (+ x 1))
  (set! x "nana")

* Commenting
  On line ; ; ; ; ;

* Procedures
  is just another type of value.
  All names belong to a single unified namespace.
  Eg: assign procedure to a shorter name
  (define call/cc call-with-current-continuation)

Form:
 (procedure [arg1 [arg2 …]])

* Lambda
A define expression of the form

(define (name [arg1 [arg2 …]])
  expression …)

is exactly equivalent to the longer form

(define name
  (lambda ([arg1 [arg2 …]])
    expression …))


* Some procedures

  (string-length)
  (string-append)

