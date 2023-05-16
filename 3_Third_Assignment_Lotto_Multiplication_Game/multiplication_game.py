
import random as r
practice_num = int(input("How many problems do you want? \n"))
correct_attempts = 0
for x in range(practice_num):
    y = (r.randrange(1,10))
    z = (r.randrange(1,10))
    answer = int(y * z)
    attempt= int(input("What is " + str(y) + " x " + str(z) + "? \n"))
    if attempt == answer:
        print ("Correct! You are so smart!")
        correct_attempts += 1
    if attempt != answer:
        print ("Inncorrect, but it is ok. Keep putting effort and believing you can do it, and you will get in no time.")
percentage_correct = float(correct_attempts / practice_num) * 100
                   
#Output
print("You got " + str(percentage_correct) + "% of the problems correct!")