#Assignment/Problem C Solution 1, Using Iterative (+1 and -1 ), Using ELIF and IF and Remainder Math
import math as mt
gas_gallons = input("How many gallons of gas does your tank hold? (Numeric Form, Max is 99 Gallons) \n")
gas_gallons = int(gas_gallons)
fuel_efficiency_mpg  = input("What is your fuel efficiency in miles per gallon? (Numeric Form, Max is 99 Mpg)\n")
fuel_efficiency_mpg  = int(fuel_efficiency_mpg)
distance_miles = input("How many miles long is your road trip? (Numeric Form, Max is 4999 Miles)\n")
distance_miles = int(distance_miles)
total_fuel = fuel_efficiency_mpg * gas_gallons
#Math Equation To Get Total Distance It Can Go Assumming Tank Is Empty At Start
refuel_no_remainder = distance_miles / total_fuel
#Math Equation To Get Remainder As A Iterative Tool For Solving Problem. 
remainder_yee = int((distance_miles / total_fuel) % distance_miles)
#Math Equation To Get Total Refuel By Subtracting Refuel No Remainder By Starting With A Full Tank
#And Adding It By Remainder Rounded And Checking Remainder Over However Many Refuels Counted Above Miles on a Full Refuel Subtracted 
total = (refuel_no_remainder - 1) + (round(remainder_yee /total_fuel))
print(total)
#Filter to Ensure It Is Over 1
if total <= 0:
    filter_total = 0
elif total <= 1:
    filter_total = 1
elif total > 1: 
    filter_total = mt.ceil(total)

print("You have to refuel " + str(filter_total) + " time(s).")

#Tested Inputs: 
#10, 30, 3600, Refuel Total = 11, Refuel = 11, Pass
#10, 44, 300, Refuel Total = -0.3181818181818182, Refuel = 0, Pass
#17, 20, 350, Refuel Total = 0.029411764705882353, Refuel = 1, Pass
#20, 40, 2000, Refuel Total = 1.5, Refuel = 2
#Ford Focus, 10, 32, 1000, Refuel Total = 1.5, Refuel = 2