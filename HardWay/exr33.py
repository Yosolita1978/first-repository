 

def while_fuct(num, i_num):
    i = 0
    numbers = []
    while i < num:
        print "At the top i is %d" %i
        numbers.append(i)

        i = i + i_num
        print "Numbers now: ", numbers
        print "At the bottom i is %d" %i
    return numbers

numbers = while_fuct(10, 2)
print "The numbers: "
for num in numbers:
    print num

