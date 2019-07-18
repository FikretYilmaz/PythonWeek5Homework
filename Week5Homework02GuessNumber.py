number ="1453"
numberList = list(number)
guess=''

while guess != number:
    minus=0
    plus=0
    try:
        guess = input("Please Enter a 4-Digit Number: ")
        if guess.isdigit()==True:
            guessList=list(guess)
            index=0
            for i in guessList:
                if guessList[index] == numberList[index]:
                    plus+=1
                elif i in numberList:
                    minus-=1
                index += 1
            if guessList == numberList:
                print(("You Von"))
            elif plus != 0 and minus != 0:
                print("+",plus," ",minus,sep="")
            elif plus != 0:
                print("+",plus)
            elif minus != 0:
                print("",minus)

        else:
            raise ValueError

    except ValueError:
        print("You Must Enter Only Numbers")
