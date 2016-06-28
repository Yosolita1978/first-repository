class List(object):

    def __init__(self):
        self.list = []
           
    def __str__(self):
         return "Your Shopping list has: %s" %(self.list)

    def add(self, item):
         if item.upper() in self.list or item.lower() in self.list:
            print "That item already exist"
            return self.list.sort()
         else:
             self.list.append(item)
             return self.list.sort()

    def remove(self, item):
        if item.upper() in self.list or item.lower() in self.list:
            self.list.remove(item)
            print "The item was removed"
            return self.list.sort()
        else:
            print "That item does not exist"


def main():
    shopping_list = List()
    item = "avocado"
    item1 = "beans"
    item2 = "pizza"
    item3 = "kale"
    shopping_list.add(item)
    print shopping_list
    shopping_list.add(item1)
    print shopping_list
    shopping_list.add(item2)
    print shopping_list
    shopping_list.add(item3)
    print shopping_list
    shopping_list.add(item3)
    print shopping_list
    shopping_list.remove(item3)
    print shopping_list
    shopping_list.remove(item3)
    print shopping_list
    shopping_list.remove(item2)
    print shopping_list

if __name__ == '__main__':
    main()