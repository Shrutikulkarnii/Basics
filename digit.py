p=input("Enter a string: ")
digit=0
letter=0
for i in p:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
    else:
        pass
print("Number of letters: ",letter)
print("Number of digits: ", digit)
