name = input("Type your name :")
print("Welcome", name, "to this adventure!")

answer = input("you are on a dirt road it has come to an end and you can go left or right. Which way would you like to go?.").lower()


if answer == "left":
    answer = input("you come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross :")

    if answer == "swim":
        print("you swam across and were eaten by an alligator.")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid optins, you lose. ")

elif answer == "right":
    answer = input("you come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger, Do you talk to them (yes/no)?")
        
        if answer == "yes":
            print("you talk to the stranger and they give you gold. You Win!")
        elif answer == "no":
            print("You ignore the stranger and they are offened and you lose!")
        else:    
           print("Not a valid optins, you lose. ")
    else:
       print("Not a valid optins, you lose. ")

print("Thank you for trying Tim")    