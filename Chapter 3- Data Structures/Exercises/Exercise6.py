'''You just found out that your new dinner table won't arrive in time for the dinner, 
and you have space for only two guests.

•Start with your program from Exercise 3-5. 
 Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. 
 Each time you pop a name from your list, 
 print a message to that person letting them know you're sorry you can't invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they're still invited.

•Use del to remove the last two names from your list, so you have an empty list. 
 Print your list to make sure you actually have an empty list at the end of your program.'''

guest = ["Ashley", "Nimshy", "Raniyath"]
print (guest[0], ", you are invited for a cousins' dinner.")
print (guest[1], ", you are invited for a cousins' dinner.")
print (guest[2], ", yopu are invited for a cousins' dinner.")
print (guest[2], "will not be able to make the dinner.")
guest[2] = "Lisni"           #Replacing an element from list using List index 
print (guest[0], ", you are invited to a cousins' dinner.")
print (guest[1], ", you are invited to a cousins' dinner.")
print (guest[2], ", you are invited to a cousins' dinner.")

print ("/n Only two members can be accommodated as there is a delay in the arrival of new dinning table.")

removed_guest = guest.pop(0)  #Removed an element from the list using pop()
print ("Sorry", removed_guest, ", you wouldn't be accommodated in the cousins' dinner party.")

print (guest[0], ", you are still invited for the cousins' dinner party.")
print (guest[1], ", you are still invited for the cousins' dinner party.")

del(guest[0])                 #Removing an element from a list using del()
del(guest[0])

print(guest)
