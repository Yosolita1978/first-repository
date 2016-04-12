# encoding: utf-8
import random

def dice():
    print random.randint(1, 6)
    prompt = "Do you want to throw again?: "
    return raw_input(prompt)

message = "Hello, I\'m going to throw the dice: "
print message
answer = dice()

while answer == "Yes" :
    answer = dice()

if answer == "No":
    print "Bummer!"
else:
    print "I don\'t understand that"
        