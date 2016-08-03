# encoding: utf-8

l = range(1,101)


for num in l:
    if num % 3 == 0 and num % 5 == 0:
        print "CracklePop"
    elif num % 5 == 0:
        print "Pop"
    elif num % 3 == 0:
        print "Crackle"
    else:
        print num
