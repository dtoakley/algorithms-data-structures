from pythonds.basic.stack import Stack

# list of list binary tree


def binary_tree(root):
    return [root, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])

    return root


def insert_right(root, new_branch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])

    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, val):
    root[0] = val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


# nodes and references binary tree

class BinaryTree(object):

    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = new_node
        else:
            new_tree = BinaryTree(new_node)
            new_tree.left_child = self.left_child
            self.left_child = new_tree

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = new_node
        else:
            new_tree = BinaryTree(new_node)
            new_tree.right_child = self.right_child
            self.right_child = new_tree

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    # tree traversal

    def pre_order(self):  # traverses the tree from the root node, recursively to the left, the recursively to the right
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()


# tree traversal - external functions

def pre_order(tree):
    if tree:
        print(tree.get_root_val())
        pre_order(tree.get_left_val())
        pre_order(tree.get_right_val())


def post_order(tree):
    if tree is not None:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.get_root_val())


def in_order(tree):
    if tree is not None:
        in_order(tree.get_left_child())
        print(tree.get_root_val())
        in_order(tree.get_right_child())



