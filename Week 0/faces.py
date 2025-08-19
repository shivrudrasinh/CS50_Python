'''
 
Problem: Implement a function called convert that accepts a str as input 
         and returns that same input with any :) converted to 🙂  and 
         any :( converted to 🙁 usings functions 
'''

def convert(text):
    text = text.replace(":)","🙂").replace(":(","🙁")
    print(text)
    
    
def main():
    n = input("How are you feeling! ")
    convert(n)
    print(n)


main()