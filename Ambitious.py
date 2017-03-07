#!/usr/bin/python

# print name one by one vertically
# Count name size (n)
# loop n times, each time printing value at index (n-1)
# very ambitious indeed

def Ambitious():
  name=raw_input("Hello, What's your name? \n")
  print
    
  counter=0
  print name[0]
  while counter<len(name)-1:
    counter=counter+1    
    print name[counter]
      


Ambitious()
 # And I've hacked it!! 
#coding really is debugging....
