#! /usr/bin/python
# counts the no. of times a certain letter appears


def count():
  count=0
  word="Banana"
  
  
  for x in word: #assingns every word in Banana to 'x' one at a time, such that there's always one x
    if x=="a":   # if the current x matches "a":            
      count=count+1 #increase count from 0 to one and so forth...
  print "The letter appears",count,"times"
  
count()
