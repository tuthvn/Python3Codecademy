def grade_converter(gpa):
  if gpa >= 4.0:
    grade = "A"
  elif gpa < 4.0 and gpa >= 3.0:
    grade = "B"
  elif gpa < 3.0 and gpa >= 2.0:
    grade = "C"
  elif gpa < 2.0 and gpa >= 1.0:
    grade = "D"
  elif gpa < 1.0 and gpa >= 0.0:
    grade = "F"
  return grade
print(grade_converter(0))
print(grade_converter(1))
print(grade_converter(2))
print(grade_converter(3))
print(grade_converter(4))