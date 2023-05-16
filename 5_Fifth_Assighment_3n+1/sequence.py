#Starting Value of N 
first_n =  int(input("Pick a number between 1-1000, inclusively \n"))
n = first_n
#Initializing Loop 
list_hold = []
print ("Enjoy the magic. \n")
#While Loop Will Iterate Until n == 1, If, Elif conditionals provide deciding if the number is even or odd
while n != 1:
    if n == 1:
        print(n)
        #Stops the Loop After N==1 
        break 
    elif n % 2 == 0:
        n = int(n / 2)
        #Appending to a list that will be extracted
        list_hold.append(n)
    elif n % 2 != 0:
        n = int((n*3) + 1)
        #Appending to a list that will be extracted
        list_hold.append(n)
#Unpacking 
for x in list_hold[:-1]:
    print(x, end =",")
print(list_hold[-1])