#!/usr/bin/env python
from random import choice
import string

strength = 8

def generatePassword(strength):
    alphabets = string.ascii_letters + string.digits
    password = ""

    for alphabet in alphabets:
        strength -= 1
        
        if (strength == 0):
            break
    
        password += choice(alphabets)

    return password

if __name__ == "__main__":
    print("""
     ____
    |  _ \ __ _ ___ ___  __ _  ___ _ __
    | |_) / _` / __/ __|/ _` |/ _ \ '_ \\ 
    |  __/ (_| \__ \__ \ (_| |  __/ | | |
    |_|   \__,_|___/___/\__, |\___|_| |_|
                        |___/
    """)
    
    strength = int(input("Enter Strength for the password: "))
    generated = generatePassword(strength)

    print(f"Generated passwdord: {generated}")
