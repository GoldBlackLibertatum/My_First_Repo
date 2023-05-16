#Solution 1
diapers_cost = float(input("What is the cost of a dozen diapers? (In Dollars) \n"))
diapers_day  = int(input("How many diapers does the baby go through a day? (Whole Number) \n"))
beer_cost = float(input("What is the cost of a single beer? \n"))

#Math Equation To Get Total Diapers In A Month
diapers_month= diapers_day * 30

#Math Equation To Get Cost of Diapers In A Month. 
diapers_cost_month = (diapers_month/12) * diapers_cost 


#Math Equation To Get Beers Reducted Subtracting By Propotional of Diapers Purchased
beers_forgon = int(diapers_cost_month - ((diapers_month/12) * (beer_cost)))

#Math Equation To Get Calories Reduced By Beers Forgon And Converted To Pounds
calories_reduced_lbs = (beers_forgon * 20) / 3500

if diapers_cost <= 3.00:
    print("You are lying about diapers costing $" + str(diapers_cost) +". Walmart sells them for a little over 8.00 for a dozen.")
else:
    print("You will spend "+ str(diapers_cost_month) + " in a month.")    
    print("You will drink " + str(beers_forgon) + " fewer beers in a month.")
    print("As a result, you will lose "+ str(calories_reduced_lbs) + " pounds in a month.")

#Test: 3.99, 9. 1.99, Output = 89.775, 45, 0.257142857148571
#Test: 2.00, 5, 2.00, Output = 25.0, 0, 0.0 [Unrealisic, beer isn't that cheap, diapers are not that cheap]
#Test: 8.50, 5, 2.50, Output = 8.50, 2.50, 0.42857142857142855