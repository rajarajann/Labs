#a method is a function that is associated with a particular class
#Methods are semantically the same as functions, but there are two syntactic differences
#Methods are defined inside a class definition in order to make the relationship between the class and the method explicit.
#The syntax for invoking a method is different from the syntax for calling a function.
#Time.print_time(start) #uncommonway of starting
def time_to_int(t):
    minutes = t.hr * 60 + t.min
    seconds = minutes * 60 + t.sec
    return seconds
#function that converts int to time:
def int_to_time(seconds):
    time = Time()
    min, time.sec = divmod(seconds, 60)
    time.hr, time.min = divmod(min, 60)
    return time
#the init method:
class Time:
    def print_time(self):
        print('%.2d'':''%.2d'':''%.2d' % (self.hr,self.min,self.sec))
    def __init__(self,hr = 0,min = 0,sec =0):
        self.hr = hr
        self.min = min
        self.sec = sec
    def __str__(self):
        return "%2d:%2d:%2d" % (self.hr,self.min,self.sec)
    def __add__(self,other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

start = Time()
start.hr = 10
start.min = 10
start.sec = 30

start.print_time() #common way #start is the object the method is invoked on, which is called the subject
atime = Time(9,45,30)
btime = Time(1,1,1)
#atime.print_time()
print(atime + btime)




