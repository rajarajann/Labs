"""Using the built-in reduce function, find the sum of the square of even numbers between 0 to 10"""
"""Generate a list with numbers 0 to 10"""
import functools
mylist = []
for i in range (11):

    if  i%2 == 0:
        mylist.append (i)

"""Square the numbers in list"""
"""def square (a):
    y = a**2
    return y"""

square_list = list(map(lambda x: x**2, mylist))

"""Using reduce function to add the squared numbers and generate the final list"""

final_list = functools.reduce(lambda x,y : x+y, square_list)
print(final_list)

