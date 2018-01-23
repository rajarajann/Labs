file = open ("words.txt")

def has_no_e (words):
    for letters in words:
        if letters == "e":
            return False
    return True

for lines in file:
    words = lines.strip()
    if has_no_e (words) == True:
        print (words)
