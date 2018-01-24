class Time:
    """represent the time of a day with attributes hours, minutes and seconds"""
time = Time()
time.hr = 11
time.min = 59
time.sec = 30

def print_time(t):
    print("Time is  ""%.2d"":""%.2d"":""%.2d" % (t.hr,t.min,t.sec))
print_time(time)

#Pure functions

def add_time(t1,t2):
    sum = Time()
    sum.hr = t1.hr + t2.hr
    sum.min = t1.min + t2.min
    sum.sec = t1.sec + t2.sec
    if sum.min > 60:
        sum.min -= 60
        sum.hr += 1
    if sum.sec > 60:
        sum.sec -= 60
        sum.min += 1
    return sum

start = Time()
start.hr = 9
start.min = 45
start.sec = 0

duration = Time()
duration.hr = 1
duration.min = 45
duration.sec = 0

end_time = add_time(start,duration)
print_time (end_time)

#Modifiers : modify the objects it gets as parameters
def increment (time, seconds):
    time.sec += seconds

    while time.sec >= 60:
        time.sec -= 60
        time.min +=1

    while time.min >= 60:
        time.min -=60
        time.hr +=1

    return time
dur = increment (duration, 300)
print_time(dur)

#function that convert time to integer

def time_to_int(t):
    minutes = t.hr * 60 + t.min
    seconds = minutes * 60 + t.sec
    return seconds
total_seconds = time_to_int(start)
print (total_seconds)

#function that converts int to time:

def int_to_time(seconds):
    time = Time()
    min, time.sec = divmod(seconds, 60)
    time.hr, time.min = divmod(min, 60)
    return time

print_time(int_to_time(total_seconds))

def add_time2(t1,t2):
    seconds = time_to_int(t1) + time_to_int (t2)
    return int_to_time(seconds)

addtime2 = add_time2(start,duration)
print_time(addtime2)

def valid_time(time):
    if time.hr < 0 or time.min < 0 or time.sec < 0:
        return False
    if time.min > 60 or time.sec > 60:
        return False
    return True

check1 = Time()
check1.hr = 11
check1.min = 30
check1.sec = 0

check2 = Time()
check2.hr = 5
check2.min = 30
check2.sec = 0

def add_time3 (t1,t2):
    assert valid_time(t1) and valid_time (t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

addtime3 = add_time3(check1,check2)
print_time(addtime3)

