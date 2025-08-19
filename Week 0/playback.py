
'''
    Problem: Implement a program in Python that prompts the user for input 
             and then outputs that same input, replacing each space  
             with ... (i.e., three periods).  
'''

msg = input("Enter your message:")
msg = msg.replace(" ","...")
print(msg)