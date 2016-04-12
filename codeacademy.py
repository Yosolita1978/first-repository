# encoding: utf-8

pyg = 'Efe'
original = raw_input('Enter a word:')


if len(original) > 0 and original.isalpha():
    word = original.lower()
    #print original
else:
    print "I don't Understand"

new_word = pyg + word 
print new_word[0:]