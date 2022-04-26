sentence = "Python is Awesome"
sentenceList = sentence.split()
print(sentenceList)
reversedSentence = ""
temp = ""
for letter in sentence:
    if letter != " ":
        temp = letter + temp
    else:
        reversedSentence = reversedSentence + temp + " "
        temp = ""
reversedSentence = reversedSentence + temp 
print(sentence)
print(reversedSentence)

