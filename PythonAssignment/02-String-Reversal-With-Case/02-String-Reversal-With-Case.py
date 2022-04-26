sentence = "Python is Awesome"
sentenceList = sentence.split()
print(sentenceList)
reversedSentence = ""
temp = ""
for letter in sentence:
    if letter != " ":
        if letter.isupper():
            letter = letter.lower()
        temp = letter + temp
    else:
        temp = temp[:1].upper() + temp[1:]
        reversedSentence = reversedSentence + temp + " "
        temp = ""
temp = temp[:1].upper() + temp[1:]
reversedSentence = reversedSentence + temp 
print(sentence)
print(reversedSentence)