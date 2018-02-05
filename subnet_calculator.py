import math
import struct
import pprint

input_ip = "10.10.10.10"
input_smask = "24"
smask = int(input_smask)

class ip_v4():
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__ (self):
        return "%d.%d.%d.%d" % (self.a,self.b,self.c,self.d)

def bin_to_int(binary_str): #['11111111', '11111111', '00000000', '00000000'] > 255.255.0.0
    dict = {}
    i = 0
    for each_element in binary_str: #its a list only
        b_sum = 0
        binary_number = each_element
        power = len (binary_number) - 1
        for digit in binary_number:
            b_sum = int(digit)*(2**power) + b_sum
            dict[i] = b_sum
            power -= 1
        i += 1
    #print (dict)
    value_list = list(dict.values())
    #print (value_list)
    ip_in_int = ip_v4(value_list[0],value_list[1],value_list[2],value_list[3])
    return(ip_in_int)

def int_to_ip(int_list): #['255','255',0,0] > 255.255.0.0
    dict = {}
    i = 0
    for element in int_list:
        dict[i] = element
        i += 1
    value_list = list(dict.values())
    in_ip_format = ip_v4(int(value_list[0]),int(value_list[1]),int(value_list[2]),int(value_list[3]))
    return (in_ip_format)

def integer_to_bin(int_argument): #255 > 11111111
    binary = "{0:0b}".format(int(int_argument))
    return binary

def intip_to_binip(int_list): #'255','255','0','0' > 11111111.11111111.0.0
    dict = {}
    i = 0
    for i in range (len(int_list)):
        dict [i] = integer_to_bin(int_list[i])
        i += 1
    value_list = list(dict.values())
    in_ip_format = ip_v4(int(value_list[0]),int(value_list[1]),int(value_list[2]),int(value_list[3]))
    return (in_ip_format)

def s_mask(smask): #got this logic from http://code.activestate.com/recipes/576483-convert-subnetmask-from-cidr-notation-to-dotdecima/
    bits = 0
    for i in range(32-smask,32):
        bits |= (1 << i)
    return "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8 , (bits & 0xff))

def wildcard(subnet_intlist):
    octet_list = []
    for octet in subnet_intlist:
        each_octet = "{0:08b}".format(255-int(octet))
        octet_list.append(each_octet)
    return (octet_list)

int_ip_list_str = input_ip.split(".") #ip is in string - ['192', '168', '1', '1']
ip_int = int_to_ip(int_ip_list_str)
ip_bin = intip_to_binip(int_ip_list_str)


int_subnet_list_str = s_mask(smask).split(".") #['255', '255', '255', '0']
subnet_int = int_to_ip(int_subnet_list_str) #255.255.255.0
subnet_bin = intip_to_binip(int_subnet_list_str) #11111111.11111111.11111111.0


wildcard_int_ip = bin_to_int (wildcard(int_subnet_list_str))
wildcard_bin = intip_to_binip(wildcard(int_subnet_list_str))
"""
wildcard_binarystr = wildcard(subnet_intlist)
print (wildcard_binarystr)
wildcard_binarylist = list(map(int,wildcard_binarystr))
print((wildcard_binarylist))
"""


print ("IP Address:",ip_int,"       ",ip_bin)
print ("Sub Net:",subnet_int,"      ",subnet_bin)
print ("Wildcard:",wildcard_int_ip,"    ",wildcard_bin)#wildcard_binarystr = wildcard(int_subnet_list_str)
#print (wildcard_binarystr)




