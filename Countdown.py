#!/usr/bin/python

#script to countdown to Blastoff for my super Jet



def Countdown(timer): 
  
  if timer==0:
    print "Super Jet has Blasted Off!"
  else:
    print timer
    Countdown(timer-1)

Countdown(10)





