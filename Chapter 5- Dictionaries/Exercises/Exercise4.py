'''Make a dictionary containing three major rivers and the country each river runs through. 
One key-value pair might be 'nile': 'egypt'.

* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

* Use a loop to print the name of each river included in the dictionary.

* Use a loop to print the name of each country included in the dictionary.
'''
river_country = {'nile': 'egypt', 
                 "Volga River": "Russia", 
                 "Yangtze River": "China", 
                 "Mississippi River": "United States"}

for river, country in river_country.items():                     #a sentence about each river
    print ("The " + river.title() + " runs through " + country.title() + ".")

print ("\n Names of Rivers included in the dictionary: ")
for river in river_country.keys():
    print ("-> " + river.title())

                  #name of each river included in the dictionary
  #  print("- " + river.title())