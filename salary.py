import sys

if len(sys.argv) == 3:
    salary = float(sys.argv[1])
    bonus_percentage = float(sys.argv[2])
else:
    salary = 20000
    bonus_percentage = 10
bonus_amount = salary * (bonus_percentage / 100)
final_salary = salary + bonus_amount

print("Salary:", salary)
print("Bonus Percentage:", bonus_percentage)
print("Final Salary:", final_salary)
