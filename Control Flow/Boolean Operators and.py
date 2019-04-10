#And
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
print(statement_one)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
print(statement_two)

def graduation_reqs(credits, gpa):
  if credits >= 120 and gpa >= 2.0:
    return "You meet the requirements to graduate!"
print(graduation_reqs(120,2))

#Or
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
print(statement_one)
statement_two = (9 + 5 <= 15) or (7 != 4 + 3)
print(statement_two)

def graduation_mailer(gpa, credits):
  if gpa >= 2.0 or credits >= 120:
    return True

#Not
statement_one = not (4 + 5 <= 9)
print(statement_one)
statement_two = not (8 * 2) != 20 - 4
print(statement_two)

def graduation_reqs1(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if not (gpa >= 2.0) and not (credits >= 120):
    return "You do not meet either requirement to graduate!"