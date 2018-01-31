import math
import struct
import pprint

input_ip = input ("Enter the IP address :")
input_smask = input ("Enter the subnet mask :")
smask = int(input_smask)

ip_str = input_ip.split(".")
print(ip_str)

ip_int = list(map(int,ip_str))
print(ip_int)

ip_bstr = ["{0:08b}".format(ip_int[0]),"{0:08b}".format(ip_int[1]),"{0:08b}".format(ip_int[2]),"{0:08b}".format(ip_int[3])]
print (ip_bstr)
ip_bin = list(map(int,ip_bstr)) #ip in binary string
print (ip_bin)

def s_mask(smask): #got this logic from http://code.activestate.com/recipes/576483-convert-subnetmask-from-cidr-notation-to-dotdecima/
    bits = 0
    for i in range(32-smask,32):
        bits |= (1 << i)
    return "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8 , (bits & 0xff))

subnetmask_int = list(map(int,s_mask(smask)))
print(subnet_mask)

class ip_v4():
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__ (self):
        return "%d.%d.%d.%d" % (self.a,self.b,self.c,self.d)

ip_binaryaddress = ip_v4(ip_bin[0],ip_bin[1],ip_bin[2],ip_bin[3])
ip_intaddress = ip_v4(ip_int[0],ip_int[1],ip_int[2],ip_int[3])
subnet = ip_v4(0,0,0,0)

print ("IP Address:",ip_intaddress,"       ",ip_binaryaddress)
print ("Sub Net:",subnet,"      ")



