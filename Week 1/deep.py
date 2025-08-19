'''
Problem : Implement a program that prompts the user for the answer to
           the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs
           42 or (case-insensitively) forty-two or forty two. Otherwise output No.

'''

text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
text = text.strip().lower()
if (text == "42" or text == "forty-two" or text == "forty two"):
    print("Yes")
else:
    print("No")
