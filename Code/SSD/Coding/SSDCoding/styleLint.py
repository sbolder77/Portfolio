# CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON
import math

#region variables
n = 4
#endregion

def factorial(n):
    """ Return factorial of n """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print("The factorial of " + str(n) + " is : " + str(math.factorial(n)))