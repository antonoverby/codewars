def get_grade(s1, s2, s3):
    grades = [s1, s2, s3]
    avg = sum(grades)/len(grades)
    print(avg)
    if avg >= 90:
        return "A"
        print("A")
    elif avg >= 80:
        return "B"
        print("B")
    elif avg >= 70:
        return "C"
        print("C")
    elif avg >= 60:
        return "D"
        print("D")
    else:
        return "F"
        print("F")
    
    

grade = get_grade(00,100,100)
print(grade)

