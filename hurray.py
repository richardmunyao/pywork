import time
def Hurray(x):
  
    
  a=0
  times=len(x)
  while times>0:
    print x[a]
    time.sleep(1)
    a=a+1
    times=times-1
  #
  #print "Hello "

def main():
  
  name=raw_input("What is your name?\n")
  print "Hello, "
  print
  Hurray(name)

if __name__ =='__main__':
  main()
