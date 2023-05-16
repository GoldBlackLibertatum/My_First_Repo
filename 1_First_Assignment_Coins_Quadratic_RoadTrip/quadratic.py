#Assignment/Problem D Solution 1, Using Sympy To Solve For X, Given A, B, C
from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
a = int(input("Please enter a from your quadratic equation\n"))
b = int(input("Please enter b from your quadratic equation\n"))
c = int(input("Please enter c from your quadratic equation\n"))
answers2 = []
answers2 = solve((a * (x**2)) + b*x + c, x)
if len(answers2) == 2:
    answers2[1] = answers2[1]
    print("The roots of your equation are " + str(answers2[0]) + " and " + str(answers2[1]) + ".")
elif len(answers2) == 1:
    print("The only root of your equation is " + str(answers2[0]) + ".")
#Tested, 1, -4, 4, X = [2]
#Tested, 1. -5, 6, X = [2,3]