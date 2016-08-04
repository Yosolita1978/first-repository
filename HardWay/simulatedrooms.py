from sys import exit

def dead(why):
    print why, "Good job!"
    exit(0)

def gold_room():
    print "This room is full of gold. How much do you want to take? "

    user_choice = raw_input("> ")
    if "0" in user_choice or "1" in user_choice:
        how_much = int(user_choice)
    else:
        dead("Man, learn to type a number")

    if how_much < 100:
        print "Nice, you're not greedy, you win!!"
        exit(0)
    else:
        dead("You, greedy bastard!")

def mirror_room():
    print "Here you see the great Enchanted Mirror."
    print "If you reflex in He, it, whatever, you go insane"
    print "Do you flee for you like or loose your head? "

    user_choice = raw_input("> ")
    if "flee" in user_choice:
        star()
    elif "loose" in user_choice:
        dead("Well, now you're crazy and be here until you starve!")
    else:
        mirror_room()

def chocolate_room():
    print "This room is full of chocolate. Do you want to eat some chocolate? "

    user_choice = raw_input("> ").lower()
    if user_choice == "yes":
        dead("The chocolate is the favorite poison of evil minds!")
    else:
        print "Nice, you're not a glutton"
        gold_room()

def dog_room():
    print "There is a big dog with three heads here."
    print "He's name is Fluffy."
    print "Fluffy is in front of the three doors of the room."
    print "How are you going to move Fluffy? "

    while True:
        user_choice = raw_input("> ")

        if "sing" in user_choice or "song" in user_choice:
            print """
            Fluffy fell asleep. You can go throught it now.
            Wich door you want to go: Left, Right or Front """
            door = raw_input("> ").lower()
        else:
            dead("Man, you have to see the Harry Potter movies")

        if door == "left":
            bigcat_room()
        elif door == "right":
            mirror_room()
        elif door == "front":
            gold_room()
        else:
            print "I got no idea what that means"

def bigcat_room():
    print "There is a big cat here."
    print "The big cat is sleeping in front the doors."
    print "How are you going to pass through the cat?"
    cat_moved = False

    while True:
        user_choice = raw_input("> ").lower()

        if user_choice == "open door":
            dead("The cat looks at you then slaps your face off")
        elif user_choice == "tiptoe" and not cat_moved:
            print "Now you're in front the doors. You can go: left, right or front "
            cat_moved = True
        elif user_choice == "walk" and cat_moved:
            dead("The cat gets pissed off and chews your legs off.")
        elif user_choice == "left" and cat_moved:
            chocolate_room()
        elif user_choice == "right" and cat_moved:
            mirror_room()
        elif user_choice == "front" and cat_moved:
            dead("The cat gets pissed off and chews your legs off.")
        else:
            print "I got no idea what that means"


def star():
    print "You are in a dark room. "
    print "There is a door to you right, left and front"
    print "Wich on do you want to take? "

    user_choice = raw_input("> ").lower()

    if user_choice == "left":
        mirror_room()
    elif user_choice == "right":
        bigcat_room()
    elif user_choice == "front":
        dog_room()
    else:
        dead("You stumble around the room until you starve. ")

def main():
    star()

if __name__ == '__main__':
    main()