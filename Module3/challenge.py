grade = 3.5
score = 65

if grade >= 3.5:
    if score >= 65:
        print(f"The student with a grade of {grade} gets a full scholarship")
    elif 50<=score<65:
        print(f"The student with a grade of {grade} and test score of {score} gets a half scholarship")
    else:
        print(f"The student with a grade of {grade} and test score of {score} is denied of a scholarship")
else:
    print(f"The student with a grade of {grade} isn't eligible of taking the test")