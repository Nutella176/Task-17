#Create a str variable, then alternate characters between lower and upper case

greeting = "Hello World"
new_greeting = ""

for i in range(len(greeting)):
    if i % 2 == 0:
        new_greeting += greeting[i].upper()
    else:
        new_greeting += greeting[i]
    
print(new_greeting)

#Alternate lower and upper case between words using split and join functions

split_greeting = greeting.split()
greeting_list = []

greeting_list.append(split_greeting[0].lower())
greeting_list.append(split_greeting[1].upper())

print(" ".join(greeting_list))
