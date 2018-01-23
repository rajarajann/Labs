file = open("words.txt")

def avoids (words,forbidden):
    for letter in words:
        if letter in forbidden:
            return False
    return True
forbidden = input ("Enter letter not to apprear: ")
count = 0
wordcount = 0
for lines in file:
    words = lines.strip()
    wordcount +=1
    if avoids(words, forbidden) == True:
        count += 1
        print (words)
print ("Total count:",count)
print ("Total word count:", wordcount)
difference = wordcount - count
print ("Difference is : ",difference)








