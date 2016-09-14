class TreeNode(object):

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def set_left(self, new_left):
        self.left = new_left

    def get_right(self):
        return self.right

    def set_right(self, new_right):
        self.right = new_right

    def __repr__(self):
        return "(%s [%s, %s])" %(self.get_data(), self.get_left(), self.get_right())

def print_tree(root, spaces=0):
    if root is None:
        return
    print "%s- %s" %(" "* spaces, root.get_data())
    print_tree(root.get_left(), spaces=spaces + 1)
    print_tree(root.get_right(), spaces=spaces +1)



def main():
    one = TreeNode(data=1)
    two = TreeNode(data=2)
    three = TreeNode(data=3)
    one.set_left(two)
    one.set_right(three)
    #print one
    four = TreeNode(data=4)
    five = TreeNode(data=5)
    two.set_left(four)
    two.set_right(five)
    print one
    print_tree(one)



if __name__ == '__main__':
    main()