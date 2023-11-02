'''Write a python code that uses three variables x, y, and z with respective values 10,20 and 30. 
Add all the variables and then store the result in variable a. Print the value of a.'''
x = 10
y = 20
z = 30
a = x+y+z
print(a)

'''Write a python program that takes courses marks as input and then calculates average of all the courses.
 After calculating the average, calculate the percentage of a student using total marks. 
 Assume the total of all the courses marks is 500 or take the total marks from the user as input. '''
cl1 = int (input("Enter the marks of Code Lab 1: "))
dvd = int (input("Enter the marks of Digital Visual Design: "))
dst = int (input("Enter the marks of Digital Storytelling: "))
sum = cl1 + dvd + dst
avg = sum/3
tot = int (input("Enter the total marks: "))
per = sum/tot *100
print(per)

'''Write a python program that takes an input 5 from user and then type cast those values to string, 
int and float in the separate variables. Print all the variables.'''
a = input("Enter your name: ")
b = input("Enter your age: ")
c = input("Enter your weight: ")
print (str(a))
print (int(b))
print (float(c))

'''Write a python program that stores an integer and string value to variables x and y. 
Print the type of variable x and y. '''
x = 100
y = "Alia"
print(type(x))
print(type(y))

'''Write a python program that stores fruit names in a list named fruits. Unpack the list into three 
variables x, y and z and then print the values of each variable.'''
fruit = ["Apple", "Mango", "Grapes"]
x = fruit[0]
y = fruit[1]
z = fruit[2]
print(x)
print(y)
print(z)
