#COP 3223 Program #1: Diaper Money

Home: https://www.cs.ucf.edu/~dmarino/ucf/transparency/cop3223/
Location:https://www.cs.ucf.edu/~dmarino/ucf/transparency/cop3223/asgn-python/ 

Arup’s life is drastically going to change because he will be a father soon. In particular, this means that he has to budget for diapers. His wife has decided that the best place to get this money from is Arup’s beer budget. In this assignment, given user input about several items, you’ll calculate the following:

1) The cost of diapers per month. (We’ll assume a month is 30 days long.)
2) The number of beers Arup won’t get to drink in a month.
3) The amount of weight Arup will lose in a month since he won’t be drinking as much beer.

You’ll ask the user to enter the following information:

1) Cost of a dozen diapers.
2) Number of diapers the baby goes through in a day.
3) The cost of a single beer.

**The constants you’ll use for this program are as follows:**

DAYS_PER_MONTH = 30
CALS_PER_LB = 3500
CALSLOST_PER_BEER = 20
DOZEN = 12

We assume that all the money spent on diapers will come out of the beer budget and however many beers this money could buy represent how many beers Arup won’t get to drink. (We will assume that the beer budget is big enough initially to handle this expense.) Finally, we assume that Arup will probably substitute beer with some other food/drink around the house, so although a beer has more than 20 calories in it, Arup will only consume 20 calories less per beer he doesn’t drink.

**Sample Program Run (User Input in Bold and Italics)**
What is the cost of a dozen diapers?
*3.99*
How many diapers does the baby go through a day?
*9*
What is the cost of a single beer?
*1.99*

*You will spend 89.775 on diapers in a month.*
*You will drink 45 fewer beers in a month.*
*As a result, you will lose 0.2571428571428571 pounds in a month.*

Calculation Notes: Calculate the diaper cost to be the prorated and print out the exact value. Calculate the number of beers to be an integer to be the greatest number of whole beers that can bought with the diaper money. 
