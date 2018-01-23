def getUniqueWords(allWords):
	uniqueWords = []
	uniqueWords.append(allWords[0])
	for i in range(len(allWords)):
	for j in range(len(uniqueWords)):
		if allWords[i] == uniqueWords[j]:
                	pass
		else:
                	uniqueWords.append(allWords[i])
                	print uniqueWords[j]
    	print uniqueWords
    	return uniqueWords
