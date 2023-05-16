#Assignment/Problem C Solution 2, Using Boolean To Iterate 
import math as mt
gas_gallons = input("How many gallons of gas does your tank hold? (Numeric Form, Max is 99 Mpg) \n")
gas_gallons = int(gas_gallons)
fuel_efficiency_mpg  = input("What is your fuel efficiency in miles per gallon? (Numeric Form, Max is 99 Mpg)\n")
fuel_efficiency_mpg  = int(fuel_efficiency_mpg)
distance_miles = input("How many miles long is your road trip? (Numeric Form, Max is 4999 Miles)\n")
distance_miles = int(distance_miles)
#Math Equation To Get Total Distance It Can Go Assumming Tank Is Empty At Start
total_fuel = fuel_efficiency_mpg * gas_gallons
#Math Equation To Get How Many Refuels Without Remainder
refuel_remainder = float((distance_miles-total_fuel) / total_fuel) 
print(refuel_remainder)

if refuel_remainder < 0:
    refuel_total = 0
    print("You have to refuel " + str(refuel_total) + " time(s)")
elif refuel_remainder > 0:
    refuel_total = mt.ceil((distance_miles-total_fuel)/ total_fuel)
    print("You have to refuel " + str(refuel_total) + " time(s)") 


#10, 30, 3600, Refuel Total = 11, Refuel = 11, Pass
#10, 44, 300, Refuel Total = -0.3181818181818182, Refuel = 0, Pass
#17, 20, 350, Refuel Total = 0.029411764705882353, Refuel = 1, Pass
#20, 40, 2000, Refuel Total = 1.5, Refuel = 2
#Ford Focus, 10, 32, 1000, Refuel Total = 1.5, Refuel = 2