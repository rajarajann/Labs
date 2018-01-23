import math
start_number = input("Enter the number to start the square root check test:")
start_number = int(start_number)
end_number = int(input("Enter the ending number for the square root check test:"))

#epsilon = 0.000000000000001
def square_root(start_number):
    x = start_number / 2
    while True:
        y = (x + start_number / x) / 2

        if y == x:

            return x
            break
        x = y


def test_square_root(start_number):
    y = math.sqrt(start_number)

    return y

square_root(start_number)
test_square_root(start_number)

print("number" ,"  Square_root","    Square_root_test","    difference")

for start_number in range (end_number):
    fun1 = square_root(start_number)
    fun2 = test_square_root(start_number)
    diff = fun1 - fun2


for start_number in range (end_number):
    print(start_number,"   ",fun1,"    ",fun2,"    ",diff)


