import math
import struct
import pprint

input_ip = "10.10.10.10"
input_smask = "16"
smask = int(input_smask)

ip_str = input_ip.split(".") #ip is in string - ['192', '168', '1', '1']
print(ip_str)
ip_int = list(map(int,ip_str)) #ip is in int list - [192, 168, 1, 1]
print(ip_int)

ip_bstr = ["{0:08b}".format(ip_int[0]),"{0:08b}".format(ip_int[1]),"{0:08b}".format(ip_int[2]),"{0:08b}".format(ip_int[3])]
print (ip_bstr) #ip is in binary string ['11000000', '10101000', '00000001', '00000001']
ip_blist = list(map(int,ip_bstr)) #ip in binary string
print (ip_blist) #ip is in binary int list [11000000, 10101000, 1, 1]

def s_mask(smask): #got this logic from http://code.activestate.com/recipes/576483-convert-subnetmask-from-cidr-notation-to-dotdecima/
    bits = 0
    for i in range(32-smask,32):
        bits |= (1 << i)
    return "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8 , (bits & 0xff))

subnet_str = s_mask(smask).split(".") #subnet is in string ['255', '255', '255', '0']
print(subnet_str)
subnet_intlist = list(map(int,subnet_str)) #subnet is in int list [255, 255, 255, 0]
print(subnet_intlist)
subnet_binarystr = ["{0:08b}".format(subnet_intlist[0]),"{0:08b}".format(subnet_intlist[1]),"{0:08b}".format(subnet_intlist[2]),"{0:08b}".format(subnet_intlist[3])]
print((subnet_binarystr[0])) #subnet is in binary string
subnet_binarylist = list(map(int,subnet_binarystr))
print((subnet_binarylist))


class ip_v4():
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__ (self):
        return "%d.%d.%d.%d" % (self.a,self.b,self.c,self.d)

ip_binaryaddress = ip_v4(ip_blist[0],ip_blist[1],ip_blist[2],ip_blist[3])
ip_intaddress = ip_v4(ip_int[0],ip_int[1],ip_int[2],ip_int[3])
subnet_binaryaddress = ip_v4(subnet_binarylist[0],subnet_binarylist[1],subnet_binarylist[2],subnet_binarylist[3])
subnet_intaddress = ip_v4(subnet_intlist[0],subnet_intlist[1],subnet_intlist[2],subnet_intlist[3])

print ("IP Address:",ip_intaddress,"       ",ip_binaryaddress)
print ("Sub Net:",subnet_intaddress,"      ",subnet_binaryaddress)

def wildcard(subnet_intlist):
    octet_list = []
    for octet in subnet_intlist:
        each_octet = "{0:08b}".format(255-int(octet))
        octet_list.append(each_octet)
    print (octet_list)

wildcard(subnet_intlist)

