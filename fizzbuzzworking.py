print "This is FizzBuzz, The Program"
my_input = raw_input("Bro, enter something!")
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
