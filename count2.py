#!/usr/bin/python
#Count version 2

def count2(x):
  word="Banana"
  index=0
  count=0
  
  while index<len(word):
    if word[index]==x:
      count=count+1
    index=index+1
  print x,"appears",count,"times"

count2("a")
