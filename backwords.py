#! /usr/bin/python
# printing letters of a name backwards one by one
# example "ABCD" len is 4. 'D'is -1 and 'A' is -4
# -1 IS GREATER THAN -4
import time
def backwards():
  counter=-1
  name=raw_input("Enter your name to print backwards \n")  
  print
  
  while counter>=-len(name): #while -1 is greater than -4(which is true..:
    print name[counter]      #print -1 (which is 'D')
    time.sleep(0.5)
    counter=counter-1        # and keep reducing to -2,-3,-4(which is 'A')
    
  print
  print "Happy Backwards Day!"
backwards()
