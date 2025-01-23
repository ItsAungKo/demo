for x in range(3):
    num = (input("Enter Number"))

    if num == "4":
        print("Yout guess is Correct!")
        exit()
    elif num == "1":
        print("Too Low!")
    elif num == "10":
        print("Too High!!!")
    else :
        print("Ran out of 3 Guess.")
    
