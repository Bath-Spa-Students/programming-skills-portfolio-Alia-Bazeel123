'''
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
As they enter each topping, print a message saying you'll add that topping to their pizza.
'''
print ("You can add toppings of your choice..")
print ("Please write 'Quit' once you finish.")

while True:
    topping = input ("Enter the topping to be added: ")
    if topping == "Quit":
        break
    else:
        print ("We'll add ", topping, "to your pizza.")
