#!/usr/bin/env python3

import operator
import readline
from colorama import init, Fore, Back, Style

operators = {
  '+': operator.add,
  '-': operator.sub,
  '*': operator.mul,
  '/': operator.truediv,
  '^': operator.pow,
  '%': operator.mod
}

def isInteger(str):
  try:
    int(str)
    return True
  except ValueError:
    return False

def isFloat(str):
  try:
    float(str)
    return True
  except ValueError:
    return False

def colorize(output):
  result = '';
  for word in output.split():

    if len(result):
      result = result + Fore.RESET + Back.RESET + ' '

    # Operators are yellow
    if (word in operators):
      result = result + Fore.YELLOW + Back.RESET + word
      continue

    # Ints are blue
    elif (isInteger(word)):
      if (int(word) >= 0):
        result = result + Fore.BLUE + Back.RESET + word
      else:
        result = result + Fore.BLUE + Back.RED + word

    # Floats are magenta
    elif (isFloat(word)):
      if (float(word) >= 0):
        result = result + Fore.MAGENTA + Back.RESET + word
      else:
        result = result + Fore.MAGENTA + Back.RED + word

    else:
      result = result + Fore.RESET + Back.RESET + word

  return result

# To demonstrate test coverage
def factorial(x):
  if x <= 1:
    return 1

  return x * factorial(x - 1)

def calculate(myarg):
  stack = list()
  for token in myarg.split():
    try:
      token = int(token)
      stack.append(token)
    except ValueError:
      function = operators[token]
      arg2 = stack.pop()
      arg1 = stack.pop()
      result = function(arg1, arg2)
      stack.append(result)
  if len(stack) != 1:
    raise TypeError("Too many parameters")
  return stack.pop()

def main():
  init(autoreset=True)
  while True:
    userInput = input("rpn calc> ")
    result = calculate(userInput)
    print(colorize(userInput))
    print(colorize(str(result)))

if __name__ == '__main__':
  main()
