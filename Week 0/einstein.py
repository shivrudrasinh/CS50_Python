'''

Problem: implement a program in Python that prompts the user for mass as an 
         integer (in kilograms) and then outputs the equivalent number of Joules 
         as an integer. Assume that the user will input an integer.

'''


def einstein():
   c = 300000000
   m = int(input("Enter mass in kilograms:"))
   E = m*(c**2)
   print(E)

einstein()   