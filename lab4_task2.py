import functools
elist = []

upper_limit = int (input("Please enter the upper limit for the number list:    "))
lower_limit = int (input("Please enter the lower limit for the number list:    "))
case = int (input("Sum of odd / even number program. Select 1 for odd, 2 for even:  "))

for i in range (upper_limit):
    if i >= lower_limit:
        if case == 2:
            if i%2==0:
                elist.append(i)
        if case == 1:
            if i%2 != 0:
                elist.append(i)

y = functools.reduce (lambda x,y : x+y,elist)
print ("The sum of all numbers between the given range is:    ",y)
