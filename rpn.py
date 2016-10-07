#!/usr/bin/env python3

def calculate(s):
  stack = []
  for token in s.split():
    if token == '+':
      arg1 = stack.pop()
      arg2 = stack.pop()
      result = arg1 + arg2
      stack.append(result)
    else:
      stack.append(int(token))
  return stack.pop()

def main():
  while True:
    calculate(input('rpn calc> '))

if __name__ == '__main__':
  main()
