#! /usr/bin/python
import time

#Countdown version 2

def Countdown(x):
  while x>0:
    print x
    time.sleep(1)
    x=(x-1)
  

Countdown(9)
