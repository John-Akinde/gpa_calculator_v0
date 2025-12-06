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
def gpa_calc():
    unit_count = 0
    unit_grade_product = 0
    unit_grade_product_total = 0
    print('enter grade and unit ')
    while True:
        score = int(input("score: "))
        unit = int(input("unit: "))
        grade = get_grade(score)
        unit_count += unit
        if grade == "A":
            unit_grade_product = unit * Grade_point["A"]
            unit_grade_product_total += unit_grade_product
        elif grade == "B":
            unit_grade_product = unit * Grade_point["B"]
            unit_grade_product_total += unit_grade_product
        elif grade == "C":
            unit_grade_product = unit * Grade_point["C"]
            unit_grade_product_total += unit_grade_product
        elif grade == "D":
            unit_grade_product = unit * Grade_point["D"]
            unit_grade_product_total += unit_grade_product
        elif grade == "F":
            unit_grade_product = unit  * Grade_point["F"]
            unit_grade_product_total += unit_grade_product
        else:
            print('invalid')

        another = input('enter another grade(y/n): ').lower().strip()
        if another == "y":
            continue
        else:
            GPA = float(unit_grade_product_total/unit_count)
            break
    return f'{GPA:.2f}'


print(f' GPA = {gpa_calc()}')



