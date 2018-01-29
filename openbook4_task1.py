fin_street = open ("Street_Centrelines.csv")
fin_busstop = open ("Bus_Stops.csv")
fout = open("out.txt",'w')


def tuple_task ():
    task_list =[]
    for line in fin_street:
        items = line.split(",")
        str_name = items[2]
        task_list.append(str_name)
        full_name = items[4]
        task_list.append(full_name)
        from_street = items [6]
        task_list.append(from_street)
        to_street = items [7]
        task_list.append(to_street)
        task_tuple = tuple(task_list)
    fin_street.close()
    print (task_tuple)

def maintenance():
    fin_street = open("Street_Centrelines.csv")
    dictionary = dict()
    for line in fin_street:
        items = line.split(",")
        if items[9] not in dictionary:
            dictionary[items[9]] = 1
        else:
            dictionary[items[9]] += 1
    print (dictionary)

def street_class():
    fin_street = open("Street_Centrelines.csv")
    dictionary = dict ()
    #str_list = []
    for line in fin_street:
        items = line.split(",")
        st_class = items[10]
        str_name = items[4]
        if st_class not in dictionary:
            dictionary[st_class] = [str_name]
            #print (type(dictionary))
        else:
            dictionary[st_class].append(str_name)
    f = str (dictionary)
    fout.write(f)
    print (dictionary)



tuple_task()
maintenance()
street_class()