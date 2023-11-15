'''A Python dictionary can be used to model an actual dictionary. 
However, to avoid confusion, let's call it a glossary.

* Think of five programming words you've learned about in the previous chapters. 
  Use these words as the keys in your glossary, and store their meanings as values.

* Print each word and its meaning as neatly formatted output. 
  You might print the word followed by a colon and then its meaning, or print 
  the word on one line and then print its meaning indented on a second line. 
  Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
'''
python_terms = {"Comment": "The line that is ignored by the interpreter.", 
            "print()": "Displays the messsege.", 
            "input()": "Takes the input/values from the user.", 
            "string": "A collection of alphabets, words or other characters enclosed in quotation marks.", 
            "in/not in": "Determine if a given value is or isn't part of a collection of values."}

print("\n Comment: ", python_terms["Comment"])
print("\n print(): ", python_terms["print()"])
print("\n input(): ", python_terms["input()"])
print("\n string: ", python_terms["string"])
print("\n in/not in: ", python_terms["in/not in"])
