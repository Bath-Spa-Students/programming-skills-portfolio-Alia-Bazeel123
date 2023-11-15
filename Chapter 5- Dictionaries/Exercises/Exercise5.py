'''Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner's name. 
Store these dictionaries in a list called pets. 
Next, loop through your list and asyou do, print everything you know about each pet
'''
'''Beagle = {"Dog": "Aqeel"}    Cockatiel = {"Parrot": "Alia"}
Ragdoll = {"Cat": "Bijuna"}    pets = [Beagle, Cockatiel, Ragdoll]  #print (pets)'''

pets = []                     #empty list
pet = {"Breed":"Beagle", 
        "Animal": "Dog", 
        "Owner": "Aqeel", 
        "Behavior": "Curious", 
        "Food": "Lean meats", 
        "Lifespan": "12-15 yrs"}
pets.append(pet)                       #adding information about the first pet 

pet = {"Breed":"Cockatiel", 
        "Animal": "Parrot", 
        "Owner": "Alia", 
        "Behavior": "Comical", 
        "Food": "Birdseed", 
        "Lifespan": "10-15 yrs"}
pets.append(pet)                         #adding information about the second pet

pet = {"Breed":"Ragdoll", 
        "Animal": "Cat", 
        "Owner": "Bijuna", 
        "Behavior": "Active", 
        "Food": "Wet and dry food", 
        "Lifespan": "12-15 yrs"}
pets.append(pet)                         #adding information about the third pet

for pet in pets:
    print ("\n Information about the pets: ")
    for key, value in pet.items():               #print info abt the pets
        print ("\t" + key + ": " + str(value))
