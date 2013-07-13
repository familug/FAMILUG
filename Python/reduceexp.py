#!/usr/bin/env python2

li = range(10)
print li

#sum of all items
print reduce(lambda x, y : x + y, li)

li = range(1,10)
#product of all items
print reduce(lambda x, y : x * y, li)

#string concate by all item
print reduce(lambda x, y : str(x) + str(y), li)
