# ask user for grade input
grade = float(input("Input the grade: "))

# evaluate the grade
if grade > 4:
    print ("This grade is Invalid!")
elif grade >= 3.3:
        print ("The grade is a Excellent!")
elif grade >= 2.3:
    print ("The grade is Good!")
elif grade >= 1.3:
    print ("The grade is Satisfactory!")
elif grade >= 1.0:
    print ("The grade is Poor!")
elif grade >= 0:
    print("The grade is a Failure!")
else:
    print("This grade is Invalid!")