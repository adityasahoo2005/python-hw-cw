#Print all alphabets in upper case and in lower case

def printalphabets():
    for i in range(65,91):
        print(chr(i),end ="  ")
    print()
    for i in range(97,123):
        print(chr(i),end="  ")

printalphabets()
