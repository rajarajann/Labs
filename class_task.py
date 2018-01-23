file = open ("Book-1.txt")
lines = file.readlines()

for words in lines:
	word = words.strip()
	print (word)
	

def uniquewords(words):
	uniquewords = []
	uniquewords.append(words[0])
	x = len (words)
	y = len (uniquewords)
	for i in range (x):
	
		if words [i] == uniquewords [i]:
			pass
		else:
			uniquewords.append == words [i]
			print (uniquewords[j])
	print (uniquewords)
	return uniquewords



uniquewords(words)
	

	


