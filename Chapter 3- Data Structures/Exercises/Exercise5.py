'''You just heard that one of your guests can't make the dinner, 
so you need to send out a new set of invitations. You'll have to think of someone else to invite.

•Start with your program from Exercise 3-4. 
 Add a print() call at the end of your program stating the name of the guest who can't make it.

•Modify your list, replacing the name of the guest who can't make it with 
 the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.'''

guest = ["Ashley", "Nimshy", "Raniyath"]
print (guest[0], ", you are invited for a cousins' dinner.")
print (guest[1], ", you are invited for a cousins' dinner.")
print (guest[2], ", yopu are invited for a cousins' dinner.")

print(guest[2], "will not be able to make the dinner.")

guest[2] = "Lisni"           #Replacing an element from list using List index 

print (guest[0], ", you are invited to a cousins' dinner.")
print (guest[1], ", you are invited to a cousins' dinner.")
print (guest[2], ", you are invited to a cousins' dinner.")
