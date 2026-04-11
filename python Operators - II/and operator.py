#Check the grade and level of coding in codingal

grade = int(input("enter ypur grade (1-10) : "))
if grade >= 1 and grade <= 3:
    print("basic level")
elif grade >= 4 and grade <= 5:
    print("intermediate level")
elif grade >= 6 and grade <= 8 :
    print("advanced level")
elif grade >= 9 and grade <= 10 :
    print("expert")
else :
    print("invalid input")
