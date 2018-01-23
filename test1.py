import math
b = int (input("Enter starting number for square root check:"))
end_number = int(input("Enter the ending number for square root check:"))

def square_root(a):
    x = a / 2
    while True:
        y = (x + a / x) / 2

        if y == x:
            return x
            break
        x = y


def test_square_root(a):
    y = math.sqrt(a)
    return y

print("number" ,"  Square_root","    Square_root_test","    difference")

while b < end_number:
    square_root(b)
    test_square_root(b)
    fun1 = square_root(b)
    fun2 = test_square_root(b)
    diff = fun1 - fun2
    print(b,"   ",fun1,"    ",fun2,"    ",diff)
    b += 1