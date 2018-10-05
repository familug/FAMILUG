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
