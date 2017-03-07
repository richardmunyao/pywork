#!/usr/bin/python

x=9
y=7
def CompareNum(x,y):
  if x > y:
    print x,"is greater than", y
  elif x<y:
    print x,"is less than", y
  else:
    print x,"is equal to" , y

def main():
  CompareNum(x,y)

if __name__ == '__main__':
  main()
 
