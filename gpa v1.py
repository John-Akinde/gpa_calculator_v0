#GPA calculator version 1

# FUNCTION to get grade based on score
def get_grade(score):
    if 70<=score<=100:
        return "A"
    elif 60<= score<70:
        return "B"
    elif 50 <= score <60:
        return "C"
    elif 45<= score < 50:
        return "D"
    elif 0 <= score < 45:
        return "F"
    else:
        return "invalid"

# Grade to point mapping
Grade_point = {
"A": 5,
"B": 4,
"C": 3,
"D": 2,
"F": 0
         }

result = [] #list storing results

def gpa_calc():
    while True:
        try:
            courses = int(input("Enter the number of courses: "))
            break
        except ValueError:
            print("Please enter a number.")
            continue

    unit_count = 0      #counts number of courses taken by units
    unit_grade_product_total = 0    #
    print('enter grade and unit ')

    for i in range(courses):
        while True:
            course = input("Enter course code: ").upper()
            if not course:
                print("Please enter a course code.")
                continue
            else:
                break
        while True:
            try:
                score = int(input("score: "))
                unit = int(input("unit: "))
                break
            except ValueError:
                print("Invalid input")
                continue

        grade = get_grade(score)
        unit_count += unit      #increment unit count by 1 for each course
        unit_grade_product = unit * Grade_point[grade]    #multiplies the unit of course and the grade point
        unit_grade_product_total += unit_grade_product
        result.append(f"Course: {course} | Score: {score} | Unit: {unit} | Grade: {grade}")  # adding result to result list
    GPA = float(unit_grade_product_total / unit_count)    # actual GPA calculation
    return f'{GPA:.2f}'


final_gpa = gpa_calc()
for r in result:
    print(r)       #prints each result for each course taken
print(f'Student\'s GPA: {final_gpa}')