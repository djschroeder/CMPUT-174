# prompt user for two grade inputs
first_grade = input("What is the first grade? ")
second_grade = input("What is the second grade? ")

# compare the results
#    - print inputs and indicate whether they are equal or not
if first_grade == second_grade:
    print (first_grade + " and " + second_grade + " are equal!")
else:
    print (first_grade + " and " + second_grade + " are NOT equal!")