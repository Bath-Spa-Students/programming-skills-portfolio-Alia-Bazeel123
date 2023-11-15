'''
Modify the make_shirt() function so that 
shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, 
and a shirt of any size with a different message.
'''
def make_shirt (size = 'Large', text_msg ='I love Python!'):
    print ("\n I'm going to make a ", size, " shirt.")
    print ('It will say, "', text_msg, '"')

make_shirt ()
make_shirt (size = 'Medium')
make_shirt ('Small', 'Keep calm and code on.')
