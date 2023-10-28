# Decision Structure
'''
sci = int(input("Enter the Science marks: "))
sst = int(input("Enter the Social Science marks: "))
mat = int(input("Enter the Maths marks: "))
eng = int(input("Enter the English marks: "))

marks = ( sci + sst + mat + eng ) / 4
score = 0
if marks > 100:
    score = 50
else:
    bonus = 0
print("Your Percentage: " + str(marks))


temp = int(input("Enter the temperature: "))
if temp < 40:
    print("Nice weather we're having.")
else:
    print("A little cold, isn't it ?")
'''

work = int (input("Enter the work exp: "))
salary = int (input("Enter the salary: "))
if salary > 2000:
    if work >= 2:
        print("You are eligible for loan.")
    else: 
        print("Sorry u r not eligible.")
else: 
    print("earning less than 2000")