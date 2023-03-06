#Ask user to input a sentence
#Print each word on a new line

sentence = input("Please input a sentence: ")
split_sentence = sentence.split()
print("\n".join(split_sentence))
