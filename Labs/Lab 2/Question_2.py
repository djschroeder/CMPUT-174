# prompt user for three grade inputs
first_grade = input("What is the first grade? ")
second_grade = input("What is the second grade? ")
third_grade = input("What is the third grade? ")

# determine which grade is the highest and print
if first_grade > second_grade and first_grade > third_grade:
    print ("The highest grade is " + first_grade)
elif second_grade > first_grade and second_grade > third_grade:
        print ("The highest grade is " + second_grade)    
elif third_grade > first_grade and second_grade < third_grade:
        print ("The highest grade is " + third_grade)

        
# additional statements could follow for equal values