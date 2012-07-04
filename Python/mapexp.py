#!/usr/bin/env python

"""
map(fun, iterable,...)
 Return a list of the results of applying the function to the items of
    the argument sequence(s).  If more than one sequence is given, the
    function is called with an argument list consisting of the corresponding
    item of each sequence, substituting None for missing values when not all
    sequences have the same length.  If the function is None, return a list of  the items of the sequence (or a list of tuples if more than one sequenc:e).

"""
li1 = [1, 2, 3, 4, 5]
li2 = [1, 2, 3, 4, 7]
li3 = [2, 3, 4, "hehe"]

#return a list of sum of corresponding element in each list
ret = map(lambda x,y : x + y, li1, li2)
print ret

ret = map(lambda x, y : str(x) + str(y), li2, li3 )
print ret

big_list = [li1, li2]
print big_list

#list of sum of each sub list
print map(sum, big_list)

#return a tubple consis of corresponding items from two list
ret = map(None, li2, li3)
print ret

#convert to list of list
ret = map(list, ret)
print ret

#flat list
la = []
for e in ret:
	la += e
print la

#flat list
ret = reduce(lambda x, y: x + y, ret)
print ret
