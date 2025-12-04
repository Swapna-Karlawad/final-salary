import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <salary> <bonus_percentage>")
    sys.exit()

salary = float(sys.argv[1])
bonus_percentage = float(sys.argv[2])

bonus_amount = salary * (bonus_percentage / 100)
final_salary = salary + bonus_amount

print("Final salary:", final_salary)
