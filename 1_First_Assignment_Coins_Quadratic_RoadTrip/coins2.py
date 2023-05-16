total_coins = input("How many coins do you have, in number form?\n")
total_coins = int(total_coins)
first_coin_name  = input("What is the name of the first type of coin?\n")
first_coin_name  = str(first_coin_name)
second_coin_name = input("What is the name of the second type of coin?\n")
second_coin_name = str(second_coin_name)
first_coin_price = input("How many cents is a "+ first_coin_name + "? \n")
first_coin_price = int(first_coin_price)/100
second_coin_price = input("How many cents is a "+ second_coin_name +"? \n")
second_coin_price = int(second_coin_price)/100
total_cost  = input("What is the value of the coins, in dollars?\n")
total_cost  = float (total_cost)
num_first_coin = ((second_coin_price * total_coins) - total_cost)/(second_coin_price - first_coin_price)
num_second_coin = total_coins - round(num_first_coin)

print("You must have " + str(round(num_first_coin)), first_coin_name +'s ' + "and", str(num_second_coin), second_coin_name +'s'+ ".")
