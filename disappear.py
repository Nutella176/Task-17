#Ask user to input a sentence
#Ask user which characters they want to make disappear
#Print sentence without those characters

sentence = input("Please enter a sentence: ")

char_to_remove = input("which characters would you like to make disappear? ")

for i in char_to_remove:
    sentence = sentence.replace(i, " ")
    
print(sentence)
        