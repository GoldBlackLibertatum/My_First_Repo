# Introduction to C - Programming Assignment #1, "Coins" under "Assignment" Column 

Home: https://www.cs.ucf.edu/~dmarino/ucf/transparency/cop3223/
Location:https://www.cs.ucf.edu/~dmarino/ucf/transparency/cop3223/asgn-python/ 

Coins, Pools and Quadratics
Due Date: Please Consult WebCourses for your section

**Objectives**
1.  To give students practice at typing in and running simple programs.
2.  To learn how to read in input from the user.
3. To learn how to use assignment statements and arithmetic expressions to make calculations



## Problem A: What Coins Do I Have (coins1.py)
Your brother is asking you for algebra help. He’s recently gotten a lot of problems of the following form:

Dave has a total of 24 coins, all of which are nickels or dimes. The value of all his coins is $1.85. How many of each coin does he have?

You’ve noticed that in many of the homework questions, the only change in the problem is the total number of coins and the value of the coins. Rather than take your brother through the problem step-by-step, you’ve decided that you’ll just write him a Python program that will ask him to enter the number of coins and their value that will then calculate the print out the number of nickels and dimes for that question.

**Input Specification**
1. The number of coins will be a positive integer.
2. The value of the coins will be represented as a positive real number in dollars.

The input will be such that there is a unique solution for the number of nickels and dimes.

**Output Specification**
Output a single statement with the following form:

You must have X nickels and Y dimes.

(Where X represents the number of nickels for the input and Y represents the number of dimes.)

**Output Sample**

Below is one sample output of running the program. Note that this sample is NOT a comprehensive test. You should test your program with different data than is shown here based on the specifications given above. In the sample run below, for clarity and ease of reading, the user input is given in italics while the program output is in bold. (Note: When you actually run your program no bold or italics should appear at all. These are simply used in this description for clarity’s sake.)

**Sample Run #1**
How many coins do you have?
*10*
What is the value of the coins, in dollars?
*0.85*
You must have 3 nickels and 7 dimes.

**Sample Run #2**
How many coins do you have?
*100*

What is the value of the coins, in dollars?
*10.00*

*You must have 0 nickels and 100 dimes.*

## Problem B: More Coins (coins2.py)
Your first program worked beautifully!!! Your brother was doing well with his algebra homework because of your program, and more importantly, he was out of your hair!

But, his teacher has recently upped the ante. Now, the teacher had generalized the type of problems he is giving. Instead of each problem containing just nickels and dimes, they contain any two arbitrary coins, where the value of the coin is given in the problem. In essence, instead of the problem having two input values, it how has four input values. A sample problem of this nature looks like the following:

Jennifer has a total of 20 coins, all of which are petals or gnomes. A petal is worth 7 cents and a gnome is worth 18 cents. The value of all of her coins is $3.05. How many of each coin does he have?

Thus, each of these problems introduces two new fictitious coins and gives their value. Write a new program to handle problems of this nature so that you brother stops bothering you again!!!


**Input Specification**
1. The number of coins will be a positive integer.
2. The value of the coins will be represented as a real number in dollars.
3. The names of both coins will be strings.
4. The values of both coins will be a positive integer, representing cents.

The input will be such that there is a unique solution for the number of each type of coin.

**Output Specification**
Output a single statement with the following form:

You must have X UNIT1 and Y UNIT2.

(where X represents the number of coins of type UNIT1 for the input and Y represents the number of coins of type UNIT2.)

**Sample Run #1**
*How many coins do you have?*
20
*What is the name of the first type of coin?*
petal
*What is the name of the second type of coin?*
gnome
*How many cents is a petal?*
7
*How many cents is a gnome?*
18
*What is the value of the coins, in dollars?*
3.05
*You must have 5 petal (s) and 15 gnome (s).*

**Sample Run #2**
*How many coins do you have?*
3
*What is the name of the first type of coin?*
A
*What is the name of the second type of coin?*
B
*How many cents is a A?*
1
*How many cents is a B?*
2
*What is the value of the coins, in dollars?*
0.03
*You must have 3 A (s) and 0 B (s).*

Note: If you figure out how to remove the space in between the name of the coin and the (s) in the output, then go ahead and do so.

## Part C: Road Trip (roadtrip.py)
You’re taking a road trip and want to calculate the number of times you’ll need to refuel to get to your destination. The information you know is the size of your gas tank in gallons, the fuel efficiency of your car in miles/gallon and the length of your road trip. Given this information, calculate the number of times you need to refuel. We will assume that you can arrive at your location on a empty tank of gas. Thus, if your tank holds enough gas to drive 300 miles and your trip is exactly 300 miles long, then you need to refuel 0 times.

**Input Specification**
1. The size of the gas tank will be a positive integer number of gallons (less than 100).
2. The fuel efficiency of your car, in miles per gallon will be a positive integer (less than 100).
3. The length of the road trip will be a positive integer, in miles, less than 5000.

**Output Specification**
Output a single statement with the following form:

You will have to refuel X time(s).
where X represents the number of times you’ll have to refuel for that trip.

**Sample Run #1**
*How many gallons of gas does your tank hold?*
10
*What is your fuel efficiency in miles per gallon?*
44
*How many miles long is your road trip?*
300
*You will have to refuel 0 time(s).*

**Sample Run #2**
*How many gallons of gas does your tank hold?*
17
*What is your fuel efficiency in miles per gallon?*
20
*How many miles long is your road trip?*
350
*You will have to refuel 1 time(s).*

## Part D: Quadratic Formula (quadratic.py)
Ask the user to enter a, b and c from the quadratic equation and print out the two roots of the equation, ax2 + bx + c = 0.

**Input Specification**
1. All three coefficients will be real numbers such that the solution to the given equation is 2 real roots.

**Output Specification**
Output a single statement with the following form:

The roots of your equation are X and Y.

(where X and Y are the two roots of the given quadratic equation and X ≤ Y.)

**Sample Run #1**
*Please enter a from your quadratic equation.*
1 
*Please enter b from your quadratic equation.*
-5 
*Please enter c from your quadratic equation.*
6
*The roots of your equation are 2.0 and 3.0.*

**Sample Run #2**
*Please enter a from your quadratic equation.*
1 
*Please enter b from your quadratic equation.*
-4 
*Please enter c from your quadratic equation.*
4
*The roots of your equation are 2.0 and 2.0.*
