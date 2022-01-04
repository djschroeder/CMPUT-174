# Course Difficulty Level Assessment

# prompt for quiz grade results
quiz_one = float(input("Enter marks for quiz 1 >"))
quiz_two = float(input("Enter marks for quiz 2 >"))

# variable assignment to int literal
pass_grade = 50
high_grade = 80

# evaluate input grades and determine level placement
if quiz_one >= high_grade <= quiz_two:
    print("Level 3")
elif quiz_one >= pass_grade <= quiz_two:
    print("Level 2")
elif quiz_one >= pass_grade or quiz_two >= pass_grade:
    if quiz_one >= pass_grade:
        print("Redo quiz2")
    else:
        print("Redo quiz1")
else:
    print("Level 1")