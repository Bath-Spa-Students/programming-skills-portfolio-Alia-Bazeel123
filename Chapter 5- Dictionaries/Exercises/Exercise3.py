'''Now that you know how to loop through a dictionary, 
clean up the code from Exercise 6-3 (page 99) by replacing your series of print() 
calls with a loop that runs through the dictionary's keys and values. 

When you're sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should automatically be included in the output.
'''
glossary = {"Comment": "The line that is ignored by the interpreter.", 
            "print()": "Displays the messsege.", 
            "input()": "Takes the input/values from the user.", 
            "string": "A collection of alphabets, words or other characters enclosed in quotation marks.", 
            "in/not in": "Determine if a given value is or isn't part of a collection of values."}

for word, definition in glossary.items():
	print (word +": " + definition + '\n')
