import random
words = ["house","salads", "luch", "cat", "yarn", "laptop", "radio", "mouse", "signal", "shelf"] 

def pick_word():
    random_word = random.choice(words)
    return random_word

def draw_blanks(word, guessed):
    secret_word = ""
    for letter in word:
        if letter in guessed:
            secret_word = secret_word + letter            
        else: 
            secret_word = secret_word + " _ " 
    return secret_word

w = pick_word()
lives = 8
guessed = []

print "Welcome to Hangman! Guess the mystery word with less than 8 mistakes!"
print draw_blanks(w, guessed)


while True:
    guess = raw_input("Guess a Letter: ")
    guess = guess.lower()

    if guess == "":
        print "Thank your for playing"
        break

    elif len(guess) > 1:
        print "Please enter just one letter"    

    elif guess in w:
        guessed.append(guess)
        blanks = draw_blanks(w, guessed)
        print "Correct", blanks 
     
        if blanks == w: 
            print "You win" 
            break

    else:
        lives = lives -1

        if lives == 0:
            print "You Lose"
            break
        else:
            print "Incorrect, Try again"



