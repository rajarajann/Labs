import math

input_ip = input ("Enter the IP address :")
input_smask = input ("Enter the subnet mask :")

ip = input_ip.split(".")
print (ip)
smask = int(input_smask)
print (type(smask))

class ip_v4():
    def __init__(self,a =0,b=0,c=0,d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def __str__ (self):
        return "%.3d .%.3d .%.3d .%.3d" % (self.a,self.b,self.c,self.d)


x = ip_v4()
print (x)




