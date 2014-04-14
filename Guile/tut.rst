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

  (string-length "hvnsweeting")
  (string-append str1 str2 str3)

* Evaluating Expressions (executing expressions)
  evaluation has two kinds of result:
    - value of the evaluated expression
    - side effects of the evaluation (effects that are not represented as
      values)

Side effect: define, set!
Values: lambda

An expression can be : piece of data (number, string ...), var name, procedure
invocation expression, Scheme's special syntactic expression

- Literal data expression: has no side effect
  data type's read syntax. Procedure has no "read syntax"

- Variable reference: has no side effect

- Procedure invocation expression:
  FORM: (PROCEDURE [ARG1 [ARG2 ..]])
    * evaluating individually the expressions: PROCEDURE, ARG1, ARG2 ..
    * calling the procedure with list of values obtained from evalutiation of
      AGR1 ARG2... Return last evaluated value


- Syntactic expressions: able to manipulate their args in an unevaluated form,
  can choose whether to evaluate any/all of the args expression.
  Eg: if, define, set!, lambda
  define, set!: they need name of vars as 1st arg. (if it evaluate that var, we
  have no var name)
  lambda: create a procedure obj that incorporates these expressions so that
  they can be evaluated in the future

* Tail calls
  Scheme is "properly tail  recursive" in certain context - do not consume stack space/ other

* Common syntax
  'let' creat an inner lexical env for the evaluation of a sequence of
  expressions
  'begin' executes a sequence of expressions in order and return last value
  'if' and 'cond'
  'and' 'or'
  'case '

Closure
-------

is the idea that a lambda expression "captures" the var bindings that are in
lexical scope at the point where the lambda expr occurs.
  resources and can therefore be used on brbitrarily large data.

Vcell (location)
Creating a var = establishing an association between a name/identifier and the
var location to which that name refers.

Environment: is a collection of associations between names and locations
Var bindings: name-location associations

Top level var: use ``define``
Local var : let
let: create a new env.

* Env chaining: local shadow top level

Lexical Scope =? dynamically scoped
---------------

is the idea that:
* an identifier always refers to the same var location
* var loc can be determined by static exam of the source code context in which
  that identifier appears, withou having to consier the flow of exec throught
  the program as a whole.

Closure
--------

(let ((s (* a b)))
(blah (* s s))
)

If the let body contains a lambda expr, the local env is not forgotten
local env associated with the procedure that is created by the lambda expr.

Because:
When GUILE interpreter evaluates a lambda expr, it stores the current
env as part of the procedure definition.
whenever that procedure is called, the interpreter reinstates the env that
is stored in the procedure definition and eval the procedure body within the
context of that env

define must be at top level, or they would not be accesible at top level

Closure is the capture of an env, containing persistent var bindings, within
the def of a procedure or a set of related procedures.

Apply method to my-account :
(my-account 'get-balance)

Beginer
scheme@(guile-user)> (< 1 2)
$29 = #t
scheme@(guile-user)> (> 1 2)
$30 = #f
========

Data type
-------

Boolean
~~~~~

#f mean false
all other and #t mean true

scheme@(guile-user)> (< 1 2)
$29 = #t
scheme@(guile-user)> (> 1 2)
$30 = #f
scheme@(guile-user)> (if 0 (+ 1 1) "no")
$16 = 2
scheme@(guile-user)> (if #f "yes" " no")
$17 = " no"

scheme@(guile-user)> (not #t)
$33 = #f
scheme@(guile-user)> (not #f)
$34 = #t

scheme@(guile-user)> (boolean? #f)
$36 = #t
scheme@(guile-user)> (boolean? 123)
$37 = #f

Number
-------

scheme@(guile-user)> (number? 123)
$38 = #t
scheme@(guile-user)> (number? "familug")
$39 = #f

integer
~~~~~~~

Abitrarily big.

$41 = 1219326311126352690000000
scheme@(guile-user)> (integer? 321)
$42 = #t
scheme@(guile-user)> (integer? 1.2)
$43 = #f

real
------
scheme@(guile-user)> (real? 1.2)
$44 = #t
scheme@(guile-user)> (real? 1)
$45 = #t

scheme@(guile-user)> (integer? (inexact->exact 23.0))
$49 = #t


exact and inexact
-------
scheme@(guile-user)> (exact? 23)
$46 = #t
scheme@(guile-user)> (exact? 23.0)
$47 = #f

