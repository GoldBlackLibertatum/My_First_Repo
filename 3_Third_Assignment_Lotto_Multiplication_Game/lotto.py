import random as r
#Deciding Number 
first_num =  int(input("Pick a number between 1-30, inclusively \n"))
second_num = int(input("Pick a number between 31-60, inclusively \n"))
#Initializing Counts and Loop
one_match = 0
two_match = 0
z_match = 0
#Random Number Generating to Create Lotto Over A Million Times
for x in range (1000000):
    y = (r.randrange(1,30))
    z = (r.randrange(31,60))
    if first_num == y and second_num == z:
        two_match += 1
    elif first_num == y:
        one_match += 1
    elif second_num == z:
        one_match += 1
    else: 
        z_match += 1
#Calculating Money Won and Lost Based On Matching Numbers 
one_match_d = 5.00 * one_match
two_match_d = 500.00 * two_match
total_spent = 1.00 * 1000000
total_gained = one_match_d + two_match_d
total = total_gained - total_spent
#Check to Make Sure Loop Added
print(one_match,two_match,z_match)

#Output#
print("You matched 1 number "+ str(one_match) + " times.")
print("You matched 2 number "+ str(two_match) + " times.")
print("You missed on both numbers " + str(z_match) + " times.")
#Output Conditioned By Loss or Win
if total_spent == total:
    print ("You are lucky. You broke even. Go buy some land or invest in stocks, bucko.")
elif total_spent < total:
    print ("You have broken the fabric of probability and reality. How did you make $"+ str(total) + ".")
elif total_spent > total:
    print ("You lost $" + str(abs(total))+ ". Maybe try looking into Telsa Stock?")