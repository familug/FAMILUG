# Scheme

## Vietnamese tutorial

- Introduction: https://pp.pymi.vn/article/scm1/
- Package management: https://pp.pymi.vn/article/scm_egg/

## Documents

- For Python programmers: http://wiki.call-cc.org/chicken-for-python-programmers
- CHICKEN Scheme homepage http://eggs.call-cc.org/
- Teach you Scheme in fixed days http://ds26gte.github.io/tyscheme/
- HTDP https://htdp.org/2003-09-26/Book/curriculum-Z-H-1.html#node_toc_start

## csi tips
`csi` command is interactive shell like `python` or `ipython`,
some tips:

- Show help for a procedure/unit (function/module)

```
(use chicken-doc)
,doc KEYWORD
```

e.g `,doc fold`

## List

### Creating
- '(a b c) ; List of symbol a b c
- '(1 2 a b) ; List of symbol 1 2 a b - 1 2 also is number
- (list 1 2 'a 'b) ; Same as above
- (iota 10) ; creates list 0->9
- (iota 5 1 2) ; creates list '(1 3 5 7 9)  ; count=5 start=1 step=2
- (for-each print (iota 10)) ; print 0->9
- (make-list 10 1) ; (1 1 1 1 1 1 1 1 1 1)
### Modifying
#### Add element to head of list
- (cons 1 '(a b c 2)) => (1 a b c 2) : CONStructing new list with 1 and the second list's elements
- (append '(a b c) '(2 3 4)) => (a b c 2 3 4) : create new list by concat two lists.


### Transforming

```scheme
(fold + 1 '(1 2 3)) ; => 7
(reduce + 1 '(1 2 3)) ; => 6 ; 1 only set when list empty
```

## String processing
There are not much string process function.

String procedures provided by unit `srfi-13`

```scheme
(use srfi-13)
(string-upcase "apymi")
OUTPUT: "APYMI"
```

Could also use many procedures in unit `irregex`

```scheme
(use irregex)
(irregex-split " " " a b c hihi")
Output: ("a" "b" "c" "hihi")
```
### Input/Ouput

Read all strings from a file:

```scheme
(use utils)
(read-all "/etc/passwd")
```

### Extension
Essential extensions:

- Unit library Basic Scheme definitions
- Unit eval Evaluation
- Unit expand Modules and macros handling
- Unit data-structures Data structures
- Unit ports I/O ports
- Unit files File and pathname operations
- Unit extras Useful utility definitions
- Unit irregex Regular expressions
- Unit srfi-1 List Library
- Unit srfi-4 Homogeneous numeric vectors
- Unit srfi-13 String library
- Unit srfi-14 Character set library
- Unit srfi-18 multithreading
- Unit srfi-69 Hashtable Library
- Unit posix Unix-like services
- Unit utils Shell scripting and file operations
- Unit tcp Basic TCP-sockets
- Unit lolevel Low-level operations

To use, just type `(use srfi-1)` for using unit srfi-1
