'''
Write a function called make_shirt() that accepts a size and 
the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.
'''
def make_shirt(size, text_msg):          #Summarizing the size of the shirt and the message printed on it.
    print("\n I'm going to make a " + size + " shirt.")
    print('It will say, "' + text_msg + '"')

make_shirt('XXL', 'Never give up!!!')
make_shirt(text_msg="Think positive get positive.", size='XL')
