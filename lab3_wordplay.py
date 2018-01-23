file = open("words.txt")

def has_no_a(words):
    for letter in words:
        if letter == "a":
            return False
    return True

for line in file:
    words = line.strip()
    if has_no_a(words) == True:
        print(words)




