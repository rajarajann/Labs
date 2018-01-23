file = open ("words.txt")

required = input ("Enter the alphabet:")

def uses_all(words, required):
    for letters in required:
        if letters not in words:
            return False
    return True

count = 0
tcount = 0
for line in file:
    tcount += 1
    words = line.strip()
    if uses_all(words, required) == True:
        count += 1
        print (words)

diff = tcount - count
print ("Total words in file is: ",tcount)
print ("Total words containing the letter is: ",count)
print ("Difference is ",diff)

