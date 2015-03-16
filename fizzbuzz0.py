import sys

print "The name of this script is {}".format(sys.argv[0])
print "User supplied {} arguments at run time".format(len(sys.argv))

for arg in sys.argv[1:]:
  print arg


my_input = raw_input("Enter something, yo!")
print my_input

for n in range (1,int(my_input)):
    if n%3 == 0 and n%5 == 0:
        print ("FizzBuzz")
    elif n%3 == 0:
        print ("Fizz")
    elif n%5 == 5:
        print ("Buzz")
    else:
        print (n)
