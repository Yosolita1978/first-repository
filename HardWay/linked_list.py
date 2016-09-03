#Code from Stephan Alleyne and Cristina Rodriguez

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __repr__(self):
        return str(self.get_data())


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        current = self.head
        linked = "[*%s]" %(self.head)
        while current and current.get_next():
            current = current.get_next()
            linked = linked + "->[%s]" %(current)
        return linked

    def append(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()

        return count

    def __getitem__(self, index):
        current = self.head
        count = 0
        if index >= self.__len__():
            raise IndexError()
        else:
            while current:
                if index == count:
                    return current.get_data()
                count += 1
                current = current.get_next()

    