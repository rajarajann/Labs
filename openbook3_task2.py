street_name = input ("Enter the street name: (Enter as exactly as possible)    ")
fin = open ("Bus_Stops.csv")
print ("List of bus stops in the same street are:   ")
for lines in fin:
    line_list = lines.split(",")
    location =line_list [6]

    if street_name in location:
        print (location)





