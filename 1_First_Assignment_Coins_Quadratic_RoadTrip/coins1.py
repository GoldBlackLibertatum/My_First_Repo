#Assignment/Problem A, Route 2
total_coins = input("How many coins do you have, in number form\n")
total_coins = int(total_coins)
total_cost  = input("What is the value of the coins, in dollars?\n")
total_cost  = float (total_cost)
nickels = ((.1 * total_coins) - total_cost)/.05
dimes = total_coins - int(nickels)
print(int(nickels), int(dimes))
 
print("You must have " + str(round(nickels)) + " nickels and " + str(dimes) + " dimes.")
