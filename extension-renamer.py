#! /usr/bin/python
import os

def renamer():
	for file in os.listdir('.'):
		origname=os.path.join('.', file)
		print (origname)  ## for debugging
		newname=origname[:-3]+'flv'
		print newname   ## for debugging
		os.rename(origname,newname)
		

renamer()
