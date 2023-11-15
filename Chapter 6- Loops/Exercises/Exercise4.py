'''Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, 
such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. 
After all the sandwiches have been made, print a message listing each sandwich that was made.
'''
sandwich_orders = ["Tuna Sandwiches", "Grilled Chicken Sandwich", "Egg Sandwich", "Seafood Sandwich"]
finished_sandwiches = []
while sandwich_orders:
    processing_orders = sandwich_orders.pop()
    print ("I made your", processing_orders, ".")
    finished_sandwiches.append(processing_orders)
print("\n")
for finished_sandwiches in finished_sandwiches:
    print (finished_sandwiches, "is made.")
