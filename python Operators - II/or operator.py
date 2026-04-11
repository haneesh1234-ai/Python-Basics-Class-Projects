greetings = input("Please send some greetings : ") 

print("No of characters we have in your greetings is: ", len(greetings))
print("First five letters in your greening are: ", greetings[0:5])


YesOrNO =input("do you want to learn string slice? if yes please enter 'y' or 'yes'")

if (YesOrNO == "y" or YesOrNO == "yes") :
    print("Great!!!")
    print("here is an example of slice in string")
    firstNum = int(input("Give a number between 0 to " + str(len(greetings) - 1)))
    secondNum = int(input("give number of letters you want to print : "))
    print("here is the sliced string :",greetings[firstNum:secondNum])
    
else :
    print("ok then bye")