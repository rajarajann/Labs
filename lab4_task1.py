a = [1,[2,3,4],5,[6,7,8],9]


def nested_sum(x):
    sum = 0
    for i in x:
        if isinstance(i,int):
            sum += i
        elif isinstance(i,list):
            sum+= nested_sum(i)
    return sum

print (nested_sum(a))