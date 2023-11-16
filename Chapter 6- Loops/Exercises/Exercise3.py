'''Write a loop that never ends, and run it. 
(To end the loop, press ctrl-C or close the window displaying the output.)
'''

while True:                                         # infinity loop with break
    n = int(input('Give me an integer: '))
    if n == 0:
        break
    print(str(n) + '*' + str(n) + '=' + str(n*n))
print('done')

'''i = 0                                                # loop that never ends
while i < 10:
    print(i)'''
print ("Enter your age to know whether you can watch this horror movie.")
while True:
    age = int (input ("Enter your age: "))
    if age < 15:
        print ("You are not allowed to watch.")
    elif age < 50:
        print ("You are allowed to watch.")
    else:
        print ("You are not allowed to watch.")
        