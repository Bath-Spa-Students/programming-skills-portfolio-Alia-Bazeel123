'''Using the list sandwich_orders from Exercise 7-8, 
make sure the sandwich 'pastrami' appears in the list at least three times. 

Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
Make sure no pastrami sandwiches end up in finished_sandwiches.
'''
sandwich_orders = ["Tuna Sandwiches", 'pastrami', "Grilled Chicken Sandwich", 
                   'pastrami', "Egg Sandwich", 'pastrami', "Seafood Sandwich"]
finished_sandwiches = []
print("We're sorry, the deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")

while sandwich_orders:
    processing_orders = sandwich_orders.pop()
    print ("I made your", processing_orders, ".")
    finished_sandwiches.append(processing_orders)
print("\n")
for finished_sandwiches in finished_sandwiches:
    print (finished_sandwiches, "is made.")
