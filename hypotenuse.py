#! /usr/bin/python

#hypotenuse: c-squared = a-squared + b-squared
#hypotenuse: root of c-squared
# I used 'input' instead of 'raw_input' because I expect an integer

import math

def Hypotenuse(a,b):
  c_squared=(a*a)+(b*b)
  c=math.sqrt(c_squared)
  print "The hypotenuse is: "+str(c)
  


def main():
  a=input("Enter the triangle LENGTH ")
  b=input("Enter the triangle HEIGHT ")
  Hypotenuse(a,b)

if __name__ == '__main__':
  main()
