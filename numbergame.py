# encoding: utf-8

from random import randint

def question():
    prompt = "Guess the number, between 1-50:  "
    return raw_input(prompt)

number = randint(1, 50) 
#print number

while True:
    answer = question()

    while not answer.isdigit(): 
        print "I don\'t understand that"
        answer = question()


    answer = int(answer)

    if answer < number :
        print "Too low"
    elif answer > number :    
        print "Too high"
    else:
        print "You Win!"
        break


#while answer == "Yes" :
    #answer = dice()

#if answer == "No":
    #print "Bummer!"
#else:
    #print "I don\'t understand that"

#print "123".isdigit()
#print "Saludos".isdigit()

#print "123" == 123
#print int("123") == 123