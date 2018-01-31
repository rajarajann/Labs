import math

input_ip = input ("Enter the IP address :")
input_smask = input ("Enter the subnet mask :")

ip_str = input_ip.split(".")
print (ip_str)
smask = int(input_smask)
ip_int = list(map(int,ip_str))
print (ip_int)

ip_bin = []
for i in range (4):
    ip_bin.append(bin(ip_int[i]))
    print (ip_bin)

ip_b = list(map(int,ip_bin))

class ip_v4():
    def __init__(self,a = ip_b[0],b =ip_b[1],c =ip_b[2],d =ip_b[3]):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.d = d
    def __str__ (self):
        return "%d .%d .%d .%d" % (self.a,self.b,self.c,self.d)



i = ip_v4()
print (i)


print (type(ip[2]))




