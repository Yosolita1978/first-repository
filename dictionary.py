# encoding: utf-8

dictionary = {}
diccionario = {}

def question():
    prompt = "What do you want to do:? "
    action = raw_input(prompt)
    return action

def add(dictionary, diccionario):
    english = raw_input("In english: ")
    spanish = raw_input("In Spanish: ")
    dictionary[english] = spanish
    diccionario[spanish] = english

def search(dictionary):
    print "What word do you want to know:? "
    english = raw_input("In english: ")
    if english in dictionary:
        print dictionary[english]
    else:    
        print "I dont have this word in the dictionary"

def buscar(diccionario):
    print "Qué palabra esta buscando:? "
    spanish = raw_input("In Spanish: ")
    if spanish in diccionario:
        print diccionario[spanish]
    else:    
        print "No tengo esta palabra en el diccionario"

print "Hi, this is you dictionary"

while True:
    action = question()

    if  action == "Add":
        add(dictionary, diccionario)
    elif action == "Search":
        search(dictionary)        
    elif action == "Buscar":
        buscar(diccionario)
    elif action == "Exit":
        break
    else:
        print "I don't understand"
