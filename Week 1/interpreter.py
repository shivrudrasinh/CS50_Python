
'''
 Problem: Implement a program that prompts the user for an arithmetic
          expression and then calculates and outputs the result as a
          floating-point value formatted to one decimal place.
'''

expression = input("Expression:")

x,y,z = expression.split()

x = float(x)
z = float(z)

if y == "+":
    result = x + z

elif y == "-":
    result = x - z

elif y == "*":
    result = x * z

elif y == "/":
    result = x / z

print(f"{result:.1f}")