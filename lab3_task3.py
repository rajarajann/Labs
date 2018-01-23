import math

def estimate_pi (k):
    sum = 0
    a = ((2*math.sqrt(2))/9801)
    for i in range (10):
        b = ((math.factorial(4*k))*(1103+26390*k))/((math.factorial(4)**4)*(396**(4*k)))
        total = a*b
        sum = sum + total
        print (sum)

    return sum





value = estimate_pi (10)
print (value)