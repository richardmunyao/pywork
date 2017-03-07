#!/usr/bin/python

##program to match numbers to names on a file and rename
##first renamed all videos to 1,2,3,4etc in order

import os


def vobrename():
  f=open('rock16names.txt','r')
  index=2
  
  while index>0 and index<47:
    for name in f:	
      for file in os.listdir('.'):
        if file==str(index):          
          origname=os.path.join('.', file)
          print origname
          newname=name
          print newname
          os.rename(origname,newname)
		
	      
		        
      index=index+1
    
	

vobrename()


