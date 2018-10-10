#short list of words
correct_words = ["data", "mac", "computer", "adobe", "apple", "design"]
wrong_words = ["samsung", "galaxy", "windows", "microsoft", "tablet", "android"]

#split sentence
sentence = input("Please enter a sentence ")
sentence_split = sentence.split()

#print error incase of wrong words, and print correct word
index = 0
for word in sentence_split:
	if word in wrong_words:
		index = wrong_words.index(word)
		check = correct_words[index]
		print("Error! Your sentence contains a wrong word: " + word + " should be " + check + ".")
	index + 1
