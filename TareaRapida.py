# encoding: utf-8

l = range (1,101)


for num in l:
    if num % 3 == 0 and num % 5 == 0:
        print "FizzBuzz"
    elif num % 5 == 0:
        print "Buzz"
    elif num % 3 == 0:
        print "Fizz"
    else:
        print num
