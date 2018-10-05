# Scheme

https://pp.pymi.vn/article/scm1/

## List

### Creating
- '(a b c) : List of symbol a b c
- '(1 2 a b) : List of symbol 1 2 a b - 1 2 also is number
- (list 1 2 'a 'b) : Same as above

### Modifying
#### Add element to head of list
- (cons 1 '(a b c 2)) => (1 a b c 2) : CONStructing new list with 1 and the second list's elements
- (append '(a b c) '(2 3 4)) => (a b c 2 3 4) : create new list by concat two lists.


## String processing
There are not much string process function.

String procedures provided by unit `srfi-13`

```scheme
(use srfi-13)
(string-upcase "apymi")
OUTPUT: "APYMI"
```
```

Could use many procedures in unit `irregex`

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
