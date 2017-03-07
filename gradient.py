#! /usr/bin/python

from __future__ import division 
import math

xa=2
xb=6
ya=3
yb=5

def slope(xa,xb,ya,yb):
  global m
  m=(ya-yb)/(xa-xb)
  print "The slope is: " +str(m)
  
def intercept(): 
  slope(xa,xb,ya,yb) 
  c=yb-(m*xb)
  print "The Y-intercept is: " +str(c)


def main():
  intercept()
   
   

if __name__ == '__main__':
  main()
  

#-----------------------NOTES--------------------------#

# used 'from __future__ import division' to prevent round-off for floats in division

#gradient = change in y / change in x: which is: (yb-ya)/(xb-xa)

# y-intercept is c. Which is c=mx-y

# I used 'global m' so that I can carry the value of 'm' over to the next function
