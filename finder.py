#!/usr/bin/python
# Finds the index of a certain letter or string in a word

def finder(string,x):
  index=0
  while index<len(string):
    if string[index]==x:
      print index   #Don't know why 'return' doesn't work
    index=index+1
  return -1  

finder("Haystack","t")
