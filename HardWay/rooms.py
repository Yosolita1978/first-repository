from sys import exit

def dead(why):
    print why, "Good job!"
    exit(0)


def gold_room():
    print "This room is full of gold. How much do you want to take"

    user_choice = raw_input("> ")
    if "0" in user_choice or "1" in user_choice:
        how_much = int(user_choice)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print "Nice, you're not greedy, you win!!"
        exit(0)
    else:
        dead("You, greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear? "
    bear_moved = False

    while True:
        user_choice = raw_input("> ")

        if user_choice == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif user_choice == "scream bear" and not bear_moved:
            print "The bear has moved from the door. You can go throught it now. "
            bear_moved = True
        elif user_choice == "scream bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif user_choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means"

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane"
    print "Do you flee for you like or eat your head? "

    user_choice = raw_input("> ")
    if "flee" in user_choice:
        star()
    elif "head" in user_choice:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()



def star():
    print "You are in a dark room. "
    print "There is a door to you right and left."
    print "Wich on do you want to take? "

    user_choice = raw_input("> ")

    if user_choice == "left":
        bear_room()
    elif user_choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve. ")

def main():
    star()

if __name__ == '__main__':
    main()

