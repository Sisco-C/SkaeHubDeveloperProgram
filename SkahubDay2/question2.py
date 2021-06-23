from math import sqrt

# Take user input
number = int(input("Enter the Number"))

sq_root = sqrt(number)
if int( sq_root*sq_root)== number:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")