#!/usr/bin/env python
from random import choice
from colorama import init
from termcolor import colored
import string

init()

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
  print(colored("""
   ____
  |  _ \ __ _ ___ ___  __ _  ___ _ __
  | |_) / _` / __/ __|/ _` |/ _ \ '_ \\ 
  |  __/ (_| \__ \__ \ (_| |  __/ | | |
  |_|   \__,_|___/___/\__, |\___|_| |_|
                      |___/
  """, "cyan"))
  
  try:
      print(colored("How strong do you want your password?", "yellow"))
      strength = int(input(colored("→ ", "yellow")))

  except ValueError:
    print(colored("ERROR: Invalid input, please enter a number", "red"))
    exit()

  generated = generatePassword(strength)

  print(colored(f"Generated password: {generated}", "green"))
