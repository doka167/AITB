import string
import random

charactersList = list(string.ascii_letters + string.digits +string.punctuation)


def passGenerate():
    
    while True:
        try:
            length = int(input("Enter password lenght:"))
        except:
            print("please enter digits only")
            continue
        if length <8 :
            print("please enter at least 8 digits:")
            continue
        break
   
    random.shuffle(charactersList)
    password = []
    for i in range(length):
        password.append(random.choice(charactersList))
    random.shuffle(password)
    print("".join(password))

    

passGenerate()
