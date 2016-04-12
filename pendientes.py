# encoding: utf-8

b_list = []

def show(b_list):
    if b_list == []:
        print "Your bucket list is empty"
    else:
        for element in b_list:
            print "* " + element

def question():
    prompt = "What do you want to do: "
    action = raw_input(prompt)
    return action

def add(b_list):
    prompt = "What do you want to add: "
    addition = raw_input(prompt)
    b_list.append(addition)

def remove(b_list):
    prompt = "What do you want to remove: "
    sustration = raw_input(prompt)
    b_list.remove(sustration)

print "Hi!, this is your bucket list: "

show(b_list)

while True:
    action = question()

    if  action == "Show":
        show(b_list)
    elif action == "Exit":
        break        
    elif action == "Add":
        add(b_list)
    elif action == "Remove":
        remove(b_list)    
    elif action == "Count":
        print len(b_list)
    elif action == "Sort":
        sus = sorted(b_list)
        show(sus)
    else:
        print "I don't understand"
