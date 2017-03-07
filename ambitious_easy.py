#easier way to print letters of a name one by one

import time

def easier():
  counter=0
  name=raw_input("What is your name? \n")
  print
  while counter<len(name):
    print name[counter]
    time.sleep(0.5)
    counter=counter+1
easier()
