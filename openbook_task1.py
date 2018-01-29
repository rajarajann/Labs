fin = open ("Bus_Stops.csv")

for lines in fin:
    line_list = lines.split(",")
    if line_list[7] == "Accessible":
        print (line_list)
