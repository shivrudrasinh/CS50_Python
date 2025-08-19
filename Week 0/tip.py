'''
  Problem : Implement a program that asks the user for the cost of a meal and a 
            tip percentage, then calculates and prints the tip amount, formatted 
            to two decimal places.”
'''

def main():
    dollor = dollor_to_float(input("Enter the price of the meal: "))
    percent = percent_to_float(input("What percentage would you like to tip? ")) 
    tip = dollor * percent
    print(f"Leave ${tip:.2f}tip")


def dollor_to_float(d):    
    return float(d.replace("$",""))

def percent_to_float(p):
    return float(p.replace("%",""))/100    

main()