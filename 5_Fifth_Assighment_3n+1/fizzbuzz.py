#Starting and End Inputs, Divisibility Inputs 
start =  int(input("At what number should the count start? (select a number between 1 and 100, inclusively) \n"))
end =  int(input("At what number should the count end? (select a number between 1 and 100, inclusively) \n"))
fizz_divis = int(input("What is the divisibility number for Fizz (select between 2 and 30, inclusively) \n"))
buzz_divis = int(input("What is the divisibility number for Buzz (select between 2 and 30, inclusively) \n"))

#Loop To Help It Go Through 
print ("Enjoy the magic. \n")
#While Loop Will Iterate Until n == 1, If, Elif conditionals provide deciding if the number is even or odd
for x in range (start, end):
    if x % fizz_divis == 0 and x % buzz_divis == 0:
        print("Fizz Buzz " + str(x) + "!")
    elif x % fizz_divis == 0: 
        print("Fizz " + str(x) + "!")
    elif x % buzz_divis == 0:
        print("Buzz " + str(x) + "!") 
    else:
        print(str(x))
print("All Done Fizzing and Buzzing Around.")