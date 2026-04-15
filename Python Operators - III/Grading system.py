#grading system

print("Enter the marks for the below subjects: ")

English = int(input("english : "))
Math = int(input("Math : "))
Ss  = int(input("ss : "))
science = int(input("science : "))
telugu = int(input("telug : "))

average = (English+Math+Ss+science+telugu)/5
print(average)

if average >= 46 and average <= 50 :
    print("A1")
elif average >= 41 and average <= 45 :
    print("A2")
elif average >= 36 and average <= 40 :
    print("B1")
elif average >= 31 and average <= 35 :
    print("B2")
elif average >= 26 and average <= 30 :
    print("C1")
elif average >= 21 and average <= 25 :
    print("C2")
elif average >= 11 and average <= 20 :
    print("D")
elif average >= 1 and average <= 10 :
    print("E")
else :
    print("invalid input")