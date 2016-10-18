#!/usr/bin/env python3

import operator

# To demonstrate test coverage
def factorial(x):
  if x <= 1:
    return 1
  return x * factorial(x - 1)

operators = {
  '+': operator.add,
  '-': operator.sub,
  '*': operator.mul,
  '/': operator.truediv,
  '^': operator.pow,
  '%': operator.mod
}

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
  while True:
    result = calculate(input("rpn calc> "))
    print(result)

if __name__ == '__main__':
  main()
