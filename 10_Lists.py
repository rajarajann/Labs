#a list is a sequence of values
#in a list, they can be any type. The values in a list are called elements or sometimes items.

alist = [1,2,3,4,5]
print (alist)
blist = ['crunchy frog','ram bladder','shark vomit']
print (blist)
#A list within another list is nested.
clist = [1,2,[3,4]]
print (clist)
empty = []
print (empty)
print (alist,blist,clist,empty)

#Lists are mutable
print (alist[0])
alist[4]=6
print (alist)
