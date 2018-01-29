fin = open ("Bus_Stops.csv")

def total_terminals():
    fin = open("Bus_Stops.csv")
    counter = 0
    for lines in fin:
         line_list = lines.split(",")
         if line_list[10] == "Terminal":
            counter +=1
    print ("Total number of Terminals :", counter)

def total_busstop():
    fin = open("Bus_Stops.csv")
    counter = 0
    for lines in fin:
        line_list = lines.split(",")
        if line_list[10] == "Conventional Transit Bus Stop":
            counter +=1

    print ("Total number of Conventional Transit Bus Stop :", counter)
total_terminals()
total_busstop()

def assessible_terminals(line_list):
    #fin = open("Bus_Stops.csv")
    counter = 0
    if line_list [7] == "Accessible":
        counter +=1
        accessible_terminals = line_list[6]
        print (accessible_terminals)
    return counter

print ("List of Accessible Terminals:")
for lines in fin:
    line_list = lines.split(",")
    assessible_terminals(line_list)

