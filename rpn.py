#!/usr/bin/env python3

import operator

operators = {
  '+': operator.add,
  '-': operator.sub,
  '*': operator.mul,
  '/': operator.truediv,
}

def calculate(s):
  stack = []
  for token in s.split():
    if token == '+':
      arg2 = stack.pop()
      arg1 = stack.pop()
      result = arg1 + arg2
      stack.append(result)
    elif token == '-':
      arg2 = stack.pop()
      arg1 = stack.pop()
      result = arg1 - arg2
      stack.append(result)
    elif token == '*':
      arg2 = stack.pop()
      arg1 = stack.pop()
      result = arg1 * arg2
      stack.append(result)
    elif token == '/':
      arg2 = stack.pop()
      arg1 = stack.pop()
      result = arg1 / arg2
      stack.append(result)
    else:
      stack.append(int(token))
  if len(stack) != 1:
    raise TypeError
  return stack.pop()

def main():
  while True:
    result = calculate(input('rpn calc> '))
    print(result)

if __name__ == '__main__':
  main()
