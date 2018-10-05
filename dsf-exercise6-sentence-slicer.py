sentence = []

#ask for a sentence
sentence = input("Please enter your sentence here: ")

sentence_lenght = len(sentence)

#calculate start and end of the sentence
start = int(sentence_lenght) * float(0.251)
end = int(sentence_lenght) * float(0.751)

#print new sentence
print(sentence[round(start):round(end)])

#advanced. split into list
sentencelist = sentence.split(" ")
sentencelist_lenght = len(sentencelist)

#calculate percentage of the sentence
start = int(sentencelist_lenght) * float(0.251)
end = int(sentencelist_lenght) * float(0.751)

#join new list
newsentence = (sentencelist[round(start):round(end)])
print(" ".join(newsentence))