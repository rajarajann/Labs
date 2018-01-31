import math

input_ip = input ("Enter the IP address :")
input_smask = input ("Enter the subnet mask :")

ip_str = input_ip.split(".")
print (ip_str)
smask = int(input_smask)
ip = list(map(int,ip_str))

print (ip)

class ip_v4():
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def __str__ (self):
        return "%.3d .%.3d .%.3d .%.3d" % (self.a,self.b,self.c,self.d)

print (type(ip[2]))




