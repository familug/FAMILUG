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




