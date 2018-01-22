class mobile_phone():
    """This is our user defined data type and operations on it"""
    mobile_name= ""
    mobile_user_name = ""
    mobile_os_name = ""
    mobile_number = ""
    """going to define a function inside class"""


raj = mobile_phone()
raj.mobile_name = "Aadhith's iPhone 7+"
raj.mobile_user_name = "Aadhith IOS"
raj.mobile_os_name = "IOS"
raj.mobile_number = "9029896688"

def print_mobile(mobile):
    print (mobile.mobile_number)

print_mobile(raj)