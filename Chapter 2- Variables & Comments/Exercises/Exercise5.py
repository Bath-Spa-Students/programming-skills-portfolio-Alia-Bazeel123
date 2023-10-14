'''A girl heads to a computer shop to buy some USB sticks. 
She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.'''

x = 50     #Amount with the girl
y = 6      #Amount for one USB stick
z = x/y
print("The girl can get",int(z),"USB sticks.")

a = int(z)*y
b = x-a
print("The amount left with the girl is",b,"pounds.")
