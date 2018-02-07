user_input_str = input("Enter the values:")
user_input_list = user_input_str.split(",")
#print(user_input)

def my_zip(x_list):
    key_list =[]
    for i in range(len(user_input_list)):
        key_list.append(i)


    zipped_list = zip(key_list, x_list)
    output_dict = dict(zipped_list)
    return (output_dict)

print(my_zip(user_input_list))
