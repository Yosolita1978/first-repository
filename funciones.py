def greet_world():
    message = "Hola Mundo"
    print message


def greet(name):
    message = "hola " + name

    print(message + "?")
    print(message + "!")

greet("Jair")
greet("Cristina")


def greet_two(name_1, name_2):
    print "Hola " + name_1 + " y " + name_2
    

greet_two("Jair", "Cristina")
greet_two("Mariana", "Cristina")
greet_two("Mariana", "Paulina")
greet_two("Paulina", "Mariana")

def position(list_, index):
    print list_[index]

l = [1, 2, 3, 4, 5]
position(l, 3)

names = ["Jair", "Cristina", "Mariana", "Paulina"]
position(names, 2)


