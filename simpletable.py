#! /usr/bin/python
#making math table revision

def table2(x): #prints single line of multiples
  length=0
  y=1
  while length<6:
    print x*y,
    length=length+1 
    y=y+1 # x times one, times two, times three etc.
  print   # on to the next line  
 
def main():  #determines the no. of times loop runs
  times=1
  x=5
  while times<5:
    table2(x)
    x=x+1
    times=times+1

if __name__ =='__main__':
  main()
  



    
