import math
def div_check():
    for i in range (1500,3500):
        a = i % 7
        b = i % 5 #anyways 15 is a multiple of 5
        while a == 0:
            if b ==0:
                i += 1
                break

            else:
                print (i)
                i += 1

div_check()