'''Write a python program that takes courses marks as input and then calculates average of all the courses.
 After calculating the average, calculate the percentage of a student using total marks. 
 Assume the total of all the courses marks is 500 or take the total marks from the user as input. '''

cl1 = int (input("Enter the marks of Code Lab 1: "))  # Taking marks from the users using input() function.
dvd = int (input("Enter the marks of Digital Visual Design: "))
dst = int (input("Enter the marks of Digital Storytelling: "))
sum = cl1 + dvd + dst                                           # Adding all the values in the variables.
avg = sum/3                                                     # Calculating average marks
tot = int (input("Enter the total marks: "))          # Taking total marks from the user using input().
per = sum/tot *100                                              # Calculating percentage
print(per)                                                      # Displaying the percentage using print().
                  # The output will be in float data type as we divided the values to find the average.
